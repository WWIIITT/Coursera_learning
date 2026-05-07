# AI for Medical Diagnosis: Chest X-Ray Classification

## 1. Data Exploration & Preventing Data Leakage

### Concepts
**Data Leakage** occurs when information from outside the training dataset is used to create the model. In medical datasets, a common cause is **Patient Overlap**—when images from the same patient appear in both the training set and the validation/test set. This leads to an artificially inflated performance metric because the model easily recognizes the patient rather than the disease.

### Methods & Codes
To prevent leakage, we check for overlapping patient IDs using Python `set` intersections:

```python
def check_for_leakage(df1, df2, patient_col='PatientId'):
    """Return True if any patients are in both df1 and df2."""
    df1_patients_unique = set(df1[patient_col].unique())
    df2_patients_unique = set(df2[patient_col].unique())
    
    patients_in_both_groups = df1_patients_unique.intersection(df2_patients_unique)
    return len(patients_in_both_groups) > 0
```
To fix the leakage, you can extract the indices of the overlapping patients and drop them using pandas `df.drop()`.

---

## 2. Image Pre-processing

### Concepts
Before feeding images to a neural network, they need to be standardized. **Standardization** means adjusting the image data such that the mean is 0 and the standard deviation is 1:

$$ x_{new} = \frac{x_i - \mu}{\sigma} $$

**Important Note on Generators**: 
- For the **Training** set, we normalize images per batch using batch statistics.
- For the **Validation/Test** set, we must not compute batch-wise statistics (because in reality, inference happens one image at a time). Instead, we use the statistics (mean, std) calculated strictly from the training set to normalize the validation/test data.

### Methods & Codes
We use Keras `ImageDataGenerator` for preprocessing and reading images directly from dataframes:

```python
from keras.preprocessing.image import ImageDataGenerator

# 1. Training Generator (Normalizes using batch statistics)
image_generator = ImageDataGenerator(
    samplewise_center=True, 
    samplewise_std_normalization=True
)

train_generator = image_generator.flow_from_dataframe(
    dataframe=train_df,
    directory="data/nih/images-small/",
    x_col="Image", 
    y_col=labels, 
    class_mode="raw", 
    batch_size=8,
    shuffle=True, 
    target_size=(320, 320)
)
```

---

## 3. Dealing with Class Imbalance: Weighted Loss

### Concepts
Medical datasets usually have a massive **class imbalance** (e.g., 99% negative cases, 1% positive cases). Standard cross-entropy loss would bias the network toward the majority class. 

To fix this, we use a **Weighted Cross-Entropy Loss Function**. 
First, we calculate class frequencies:
$$ freq_{p} = \frac{\text{number of positive examples}}{N} $$
$$ freq_{n} = \frac{\text{number of negative examples}}{N} $$

Then, we inversely weight the loss classes:
$$ weight_{pos} = freq_{n} $$
$$ weight_{neg} = freq_{p} $$

**Weighted Loss Formula** for the $i^{th}$ example across classes:
$$ \mathcal{L}^{(i)}_{pos} = - weight_{pos} \times y^{(i)} \log(\hat{y}^{(i)} + \epsilon) $$
$$ \mathcal{L}^{(i)}_{neg} = - weight_{neg} \times (1-y^{(i)}) \log(1-\hat{y}^{(i)} + \epsilon) $$
$$ \mathcal{L}^{(i)} = \mathcal{L}^{(i)}_{pos} + \mathcal{L}^{(i)}_{neg} $$

*(We add an incredibly small term $\epsilon$ inside the log to avoid calculating the log of 0).*

### Methods & Codes

```python
import keras.backend as K
import numpy as np

# 1. Calculate class frequencies
def compute_class_freqs(labels):
    N = labels.shape[0]
    positive_frequencies = np.sum(labels == 1, axis=0) / N
    negative_frequencies = np.sum(labels == 0, axis=0) / N
    return positive_frequencies, negative_frequencies

# Calculate Weights
pos_weights = neg_freqs # Inverse weighting
neg_weights = pos_freqs

# 2. Weighted Loss Function in Keras
def get_weighted_loss(pos_weights, neg_weights, epsilon=1e-7):
    def weighted_loss(y_true, y_pred):
        loss = 0.0
        for i in range(len(pos_weights)):
            # Calculate loss for each class and sum them up
            loss += -1 * K.mean(
                pos_weights[i] * y_true[:, i] * K.log(y_pred[:, i] + epsilon) +
                neg_weights[i] * (1 - y_true[:, i]) * K.log(1 - y_pred[:, i] + epsilon)
            )
        return loss
    return weighted_loss
```

---

## 4. Modeling: DenseNet121

### Concepts
**DenseNet (Densely Connected Convolutional Networks)** is used as the base pre-trained model. In DenseNet, every layer is connected directly to every other deeper layer. This alleviates the vanishing gradient problem, strengthens feature propagation, and massively reduces the number of parameters.

We use **Transfer Learning**, freezing the base layers of the pre-trained DenseNet and adding a custom classification head (a Global Average Pooling layer followed by a Dense layer with a Sigmoid activation to deal with multi-label classification).

### Methods & Codes

```python
from keras.applications.densenet import DenseNet121
from keras.layers import Dense, GlobalAveragePooling2D
from keras.models import Model

# 1. Load Pre-trained Base Model
base_model = DenseNet121(weights='./models/nih/densenet.hdf5', include_top=False)

x = base_model.output

# 2. Add custom top layers
x_pool = GlobalAveragePooling2D()(x)
predictions = Dense(len(labels), activation="sigmoid")(x_pool)

# 3. Create the final compiled model
model = Model(inputs=base_model.input, outputs=predictions)

model.compile(
    optimizer='adam',
    loss=get_weighted_loss(pos_weights, neg_weights)
)
```