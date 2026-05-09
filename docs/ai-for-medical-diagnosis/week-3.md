# Week 3 - Brain Tumor Auto-Segmentation

<span class="track-badge medical">AI for Medical Diagnosis</span>

## What This Covers

Week 3 moves from image-level classification to voxel-level segmentation. The assignment uses MRI volumes from the BraTS-style brain tumor dataset, extracts smaller 3D sub-volumes, standardizes each MRI channel, trains a 3D U-Net, and evaluates segmentation quality with Dice-based metrics plus class-specific sensitivity and specificity.

The pretrained A3 model weights can be downloaded from:

[https://huggingface.co/WWWIIITTT/UNet-3D/blob/main/model_pretrained.hdf5](https://huggingface.co/WWWIIITTT/UNet-3D/blob/main/model_pretrained.hdf5)

## Core Ideas

- MRI examples are 3D volumes, not flat 2D images.
- Each MRI case contains multiple imaging channels: FLAIR, T1, T1-Gd, and T2.
- The label volume assigns one class to each voxel: background, edema, non-enhancing tumor, or enhancing tumor.
- Segmentation predicts a label for every voxel, so the model output has spatial dimensions.
- Whole MRI volumes are large, so the assignment trains on random sub-volumes of shape \(160 \times 160 \times 16\).
- The background class dominates most patches, so sampled patches are rejected when the background ratio is too high.
- Labels are converted to one-hot tensors and the background class is removed for training.
- A 3D U-Net is used because it combines local convolutional features with encoder-decoder skip connections.
- Dice coefficient measures overlap between predicted and true masks, which is better suited than accuracy for imbalanced segmentation masks.
- Soft Dice loss is differentiable and can be used directly during training.

## Data Shapes

The original MRI image has shape:

```text
(240, 240, 155, 4)
```

Where:

- \(240, 240, 155\) are the spatial \(x, y, z\) dimensions.
- `4` is the number of MRI channels.

The original label has shape:

```text
(240, 240, 155)
```

Each label voxel stores one integer class:

```text
0 = background
1 = edema
2 = non-enhancing tumor
3 = enhancing tumor
```

After patch extraction and axis movement, the model input patch has shape:

```text
(4, 160, 160, 16)
```

The training label patch has shape:

```text
(3, 160, 160, 16)
```

The label has 3 channels because the background channel is removed after one-hot encoding.

## Important Formulas

Per-slice standardization subtracts the mean and divides by the standard deviation for each MRI channel and each \(z\)-slice.

\[
x_{\text{standardized}} = \frac{x - \mu_{c,z}}{\sigma_{c,z}}
\]

Where:

- \(x\) is a voxel value in one channel and one slice.
- \(\mu_{c,z}\) is the mean for channel \(c\), slice \(z\).
- \(\sigma_{c,z}\) is the standard deviation for channel \(c\), slice \(z\).

The background ratio is the fraction of voxels in a patch that belong to the background class.

\[
\text{background ratio} =
\frac{\sum y_{\text{background}}}{\text{output}_x \times \text{output}_y \times \text{output}_z}
\]

Single-class Dice coefficient measures overlap between one predicted mask and one true mask.

\[
\text{Dice} =
\frac{2 \sum y_{\text{true}} y_{\text{pred}} + \epsilon}
{\sum y_{\text{true}} + \sum y_{\text{pred}} + \epsilon}
\]

Multi-class Dice coefficient averages Dice over the abnormality classes.

\[
\text{Mean Dice} =
\frac{1}{C} \sum_{c=1}^{C}
\frac{2 \sum y_{\text{true},c} y_{\text{pred},c} + \epsilon}
{\sum y_{\text{true},c} + \sum y_{\text{pred},c} + \epsilon}
\]

Soft Dice loss uses probabilities instead of hard binary masks and is minimized during training.

\[
\text{Soft Dice Loss} =
1 -
\frac{1}{C} \sum_{c=1}^{C}
\frac{2 \sum y_{\text{true},c} y_{\text{pred},c} + \epsilon}
{\sum y_{\text{true},c}^{2} + \sum y_{\text{pred},c}^{2} + \epsilon}
\]

Sensitivity for one segmentation class measures how many true positive voxels were found.

\[
\text{Sensitivity} = \frac{TP}{TP + FN}
\]

Specificity for one segmentation class measures how many true negative voxels were correctly left out.

\[
\text{Specificity} = \frac{TN}{TN + FP}
\]

Where:

- \(TP\): voxel is predicted positive and truly positive.
- \(TN\): voxel is predicted negative and truly negative.
- \(FP\): voxel is predicted positive but truly negative.
- \(FN\): voxel is predicted negative but truly positive.

## Human-Readable Explanation

Classification asks whether a disease is present in an image. Segmentation asks where the disease is. In Week 3, the model must label every voxel in a brain MRI volume as edema, non-enhancing tumor, enhancing tumor, or background.

The raw data is too large to use as full volumes during ordinary training, so the notebook samples smaller 3D patches. A random corner is chosen, a patch is extracted, and the label patch is one-hot encoded. If the patch is mostly background, it is rejected and another patch is sampled. This makes training examples more informative because the model sees enough tumor voxels to learn from.

The MRI channels can have different intensity distributions. The standardization step normalizes each channel and slice separately so the model sees values on a more stable scale.

The 3D U-Net uses an encoder to compress the volume into deeper features and a decoder to recover the spatial resolution. Skip connections concatenate encoder features with decoder features at matching resolutions. This helps the model combine semantic context with precise localization.

Accuracy is weak for segmentation because a model could predict background for nearly every voxel and still look good. Dice coefficient focuses on overlap between predicted and true tumor regions, so it is more aligned with the segmentation goal.

## Key Code Patterns

Extract a useful random sub-volume:

```python
def get_sub_volume(image, label,
                   orig_x=240, orig_y=240, orig_z=155,
                   output_x=160, output_y=160, output_z=16,
                   num_classes=4, max_tries=1000,
                   background_threshold=0.95):
    X = None
    y = None
    tries = 0

    while tries < max_tries:
        start_x = np.random.randint(0, orig_x - output_x + 1)
        start_y = np.random.randint(0, orig_y - output_y + 1)
        start_z = np.random.randint(0, orig_z - output_z + 1)

        y = label[start_x:start_x + output_x,
                  start_y:start_y + output_y,
                  start_z:start_z + output_z]

        y = keras.utils.to_categorical(y, num_classes=num_classes)
        bgrd_ratio = np.sum(y[:, :, :, 0]) / (output_x * output_y * output_z)
        tries += 1

        if bgrd_ratio < background_threshold:
            X = np.copy(image[start_x:start_x + output_x,
                              start_y:start_y + output_y,
                              start_z:start_z + output_z, :])

            X = np.moveaxis(X, -1, 0)
            y = np.moveaxis(y, -1, 0)
            y = y[1:, :, :, :]

            return X, y

    print(f"Tried {tries} times to find a sub-volume. Giving up...")
```

Standardize every channel and \(z\)-slice:

```python
def standardize(image):
    standardized_image = np.zeros(image.shape)

    for c in range(image.shape[0]):
        for z in range(image.shape[3]):
            image_slice = image[c, :, :, z]
            centered = image_slice - np.mean(image_slice)
            centered_scaled = centered

            if np.std(centered) != 0:
                centered_scaled = centered / np.std(centered)

            standardized_image[c, :, :, z] = centered_scaled

    return standardized_image
```

Compute Dice for one class:

```python
def single_class_dice_coefficient(y_true, y_pred, axis=(0, 1, 2),
                                  epsilon=0.00001):
    dice_numerator = 2 * K.sum(y_true * y_pred, axis=axis) + epsilon
    dice_denominator = K.sum(y_true, axis=axis) + K.sum(y_pred, axis=axis) + epsilon
    dice_coefficient = dice_numerator / dice_denominator
    return dice_coefficient
```

Compute mean Dice across classes:

```python
def dice_coefficient(y_true, y_pred, axis=(1, 2, 3), epsilon=0.00001):
    dice_numerator = 2 * K.sum(y_true * y_pred, axis=axis) + epsilon
    dice_denominator = K.sum(y_true, axis=axis) + K.sum(y_pred, axis=axis) + epsilon
    dice_coefficient = K.mean(dice_numerator / dice_denominator)
    return dice_coefficient
```

Compute Soft Dice loss:

```python
def soft_dice_loss(y_true, y_pred, axis=(1, 2, 3), epsilon=0.00001):
    dice_numerator = 2 * K.sum(y_true * y_pred, axis=axis) + epsilon
    dice_denominator = (
        K.sum(y_true * y_true, axis=axis)
        + K.sum(y_pred * y_pred, axis=axis)
        + epsilon
    )
    dice_loss = 1 - K.mean(dice_numerator / dice_denominator)
    return dice_loss
```

Compute sensitivity and specificity for one class:

```python
def compute_class_sens_spec(pred, label, class_num):
    class_pred = pred[class_num]
    class_label = label[class_num]

    tp = np.sum((class_pred == 1) & (class_label == 1))
    tn = np.sum((class_pred == 0) & (class_label == 0))
    fp = np.sum((class_pred == 1) & (class_label == 0))
    fn = np.sum((class_pred == 0) & (class_label == 1))

    sensitivity = tp / (tp + fn)
    specificity = tn / (tn + fp)

    return sensitivity, specificity
```

Build the 3D U-Net:

```python
model = util.unet_model_3d(
    loss_function=soft_dice_loss,
    metrics=[dice_coefficient],
    input_shape=(4, 160, 160, 16),
    n_labels=3
)
```

Load the pretrained A3 weights:

```python
model.load_weights("model_pretrained.hdf5")
```

The same file is available here:

```text
https://huggingface.co/WWWIIITTT/UNet-3D/blob/main/model_pretrained.hdf5
```

Generate batches from preprocessed `.h5` patches:

```python
class VolumeDataGenerator(keras.utils.Sequence):
    def __getitem__(self, index):
        indexes = self.indexes[index * self.batch_size:(index + 1) * self.batch_size]
        sample_list_temp = [self.sample_list[k] for k in indexes]
        X, y = self.__data_generation(sample_list_temp)
        return X, y

    def __data_generation(self, list_IDs_temp):
        X = np.zeros((self.batch_size, self.num_channels, *self.dim))
        y = np.zeros((self.batch_size, self.num_classes, *self.dim))

        for i, ID in enumerate(list_IDs_temp):
            with h5py.File(self.base_dir + ID, "r") as f:
                X[i] = np.array(f.get("x"))
                y[i] = np.moveaxis(np.array(f.get("y")), 3, 0)[1:]

        return X, y
```

## Model Architecture Notes

The A3 model is a 3D U-Net with channels-first tensors:

```python
K.set_image_data_format("channels_first")
```

The encoder repeatedly applies:

```text
Conv3D -> ReLU -> Conv3D -> ReLU -> MaxPooling3D
```

The decoder repeatedly applies:

```text
UpSampling3D -> Concatenate skip connection -> Conv3D -> ReLU -> Conv3D -> ReLU
```

The final layer is a \(1 \times 1 \times 1\) 3D convolution that maps features to the 3 abnormality labels:

```python
final_convolution = Conv3D(n_labels, (1, 1, 1))(current_layer)
output = Activation("sigmoid")(final_convolution)
```

Sigmoid is used because each abnormality channel is treated as an independent binary mask.

## Common Mistakes

- Forgetting that `np.random.randint` excludes the upper bound.
- Sampling with `orig_x - output_x` instead of `orig_x - output_x + 1`.
- Leaving labels in integer format instead of one-hot encoding them.
- Forgetting to remove the background class after moving the label axis.
- Using the wrong axis order: the model expects channels first.
- Standardizing the whole volume at once instead of each channel and \(z\)-slice.
- Computing Dice with ordinary NumPy when the loss needs Keras backend operations.
- Using a hard Dice formula as the training loss instead of Soft Dice loss.
- Reporting only voxel accuracy even though background voxels dominate.

## Takeaways

Week 3 extends diagnostic modeling from predicting disease presence to locating disease in 3D. The central workflow is: load MRI volumes, sample useful patches, normalize each channel and slice, train a 3D U-Net with Soft Dice loss, and evaluate the predicted masks with Dice, sensitivity, and specificity.
