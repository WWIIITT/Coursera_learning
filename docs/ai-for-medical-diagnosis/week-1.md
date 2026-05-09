# Week 1 - Chest X-Ray Diagnosis Pipeline

<span class="track-badge medical">AI for Medical Diagnosis</span>

## What This Covers

Week 1 covers the first half of the chest X-ray diagnosis workflow: data exploration, image preprocessing, patient overlap, class imbalance, weighted loss, DenseNet121, and transfer learning for multi-label classification.

## Core Ideas

- Chest X-ray data contains images, patient identifiers, and multiple disease labels.
- Patient overlap is a serious data leakage risk because the model may memorize patient-level features.
- Images need consistent size and normalization before entering a neural network.
- Medical labels are imbalanced, so rare positive cases need enough loss signal.
- DenseNet121 is used as a feature extractor, and a sigmoid output layer produces independent disease probabilities.

## Important Formulas

Standardization means subtracting the mean and dividing by the standard deviation so pixel values are on a comparable scale.

\[
x_{\text{standardized}} = \frac{x - \mu}{\sigma}
\]

Where:

- \(x\) is the original pixel value.
- \(\mu\) is the mean pixel value.
- \(\sigma\) is the standard deviation.
- \(x_{\text{standardized}}\) is the normalized pixel value.

Positive class frequency means the fraction of training examples where a disease is present.

\[
f_{\text{pos}} = \frac{\text{number of positive examples}}{N}
\]

Negative class frequency means the fraction of training examples where a disease is absent.

\[
f_{\text{neg}} = \frac{\text{number of negative examples}}{N}
\]

Where:

- \(N\) is the total number of training examples.
- \(f_{\text{pos}}\) is the positive frequency.
- \(f_{\text{neg}}\) is the negative frequency.

The class weights use the opposite class frequency so that the minority side gets more influence.

\[
w_{\text{pos}} = f_{\text{neg}}
\]

\[
w_{\text{neg}} = f_{\text{pos}}
\]

Where:

- \(w_{\text{pos}}\) is the weight applied when the true label is positive.
- \(w_{\text{neg}}\) is the weight applied when the true label is negative.

Weighted binary cross-entropy means positive and negative errors are scaled by their class weights.

\[
L = -w_{\text{pos}} y \log(\hat{y} + \epsilon) - w_{\text{neg}}(1-y)\log(1-\hat{y}+\epsilon)
\]

Where:

- \(L\) is the weighted loss for one label.
- \(y\) is the true label, either 0 or 1.
- \(\hat{y}\) is the model's predicted probability.
- \(\epsilon\) is a tiny number added to avoid taking \(\log(0)\).

## Human-Readable Explanation

The workflow begins with simple but important questions: how many examples exist for each disease, how many positive labels are available, and whether the split accidentally includes the same patient in multiple groups. These checks matter because medical models are often evaluated on rare events, and leakage can hide weak generalization.

The preprocessing step uses image generators to resize and normalize images. Training images can be transformed and normalized during training, but validation and test examples should be processed consistently using training-derived statistics. This simulates real inference more honestly.

The weighted loss addresses imbalance. If a disease is rare, a model can look good by predicting "not present" most of the time. Weighted loss makes mistakes on the rare side more expensive, giving the model a reason to learn those findings.

DenseNet121 provides a pretrained visual backbone. The course uses transfer learning by attaching a global average pooling layer and a sigmoid classifier head. Sigmoid is used because the task is multi-label: each disease is predicted independently.

## Key Code Patterns

Compute class frequencies:

```python
def compute_class_freqs(labels):
    n = labels.shape[0]
    pos_freqs = np.sum(labels == 1, axis=0) / n
    neg_freqs = np.sum(labels == 0, axis=0) / n
    return pos_freqs, neg_freqs
```

Build a weighted loss closure:

```python
def get_weighted_loss(pos_weights, neg_weights, epsilon=1e-7):
    def weighted_loss(y_true, y_pred):
        loss = 0.0
        for i in range(len(pos_weights)):
            loss += -K.mean(
                pos_weights[i] * y_true[:, i] * K.log(y_pred[:, i] + epsilon)
                + neg_weights[i] * (1 - y_true[:, i]) * K.log(1 - y_pred[:, i] + epsilon)
            )
        return loss
    return weighted_loss
```

Attach a classification head to DenseNet:

```python
base_model = DenseNet121(weights="./models/nih/densenet.hdf5", include_top=False)
x = GlobalAveragePooling2D()(base_model.output)
predictions = Dense(len(labels), activation="sigmoid")(x)
model = Model(inputs=base_model.input, outputs=predictions)
```

## Detailed Study Notes

A chest X-ray diagnosis model starts with data hygiene. The same patient can have multiple images, so a random image-level split can leak patient-specific information into validation or test data. Patient-level overlap checks should happen before model training.

The label matrix is multi-label:

```python
labels = train_df[disease_names].values
```

Each row belongs to one image, and each column belongs to one disease. A row may contain several `1` values because diseases are not mutually exclusive. That is why the final layer uses `sigmoid` instead of `softmax`.

Weighted loss changes how mistakes contribute to training:

```python
positive_loss = pos_weights[i] * y_true[:, i] * K.log(y_pred[:, i] + epsilon)
negative_loss = neg_weights[i] * (1 - y_true[:, i]) * K.log(1 - y_pred[:, i] + epsilon)
```

If positive examples are rare, the positive class receives more relative signal. This does not guarantee good sensitivity, but it prevents the loss from being dominated by common negative labels.

Transfer learning uses DenseNet as a visual feature extractor. The pretrained convolutional layers provide general image features, while the new classifier head learns the course-specific disease labels. The model should still be evaluated carefully because medical image distributions differ from ordinary natural images.

## Common Mistakes

- Using image-level splits instead of patient-level splits.
- Computing validation preprocessing statistics from validation examples.
- Using softmax for multi-label classification when diseases are not mutually exclusive.
- Forgetting the epsilon term in the logarithm.
- Assuming class weights fix all imbalance problems without checking evaluation metrics.

## Takeaways

Week 1 builds the model foundation. A trustworthy medical imaging model depends as much on data hygiene and loss design as on the neural network architecture.
