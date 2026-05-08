# AI for Medical Diagnosis

## What This Covers

This course track follows a medical image classification workflow. Week 1 builds the chest X-ray model pipeline: explore labels, prevent leakage, preprocess images, handle class imbalance, and use DenseNet for multi-label disease prediction. Week 2 evaluates the model with diagnostic metrics that are more clinically meaningful than accuracy alone.

## Core Ideas

- Medical datasets often contain multiple images per patient, so train, validation, and test splits must be checked at the patient level.
- Chest X-ray labels are multi-label: one image can have more than one disease finding.
- Class imbalance is normal in medical data because many diseases are rare.
- Weighted loss helps the model avoid learning only the majority class.
- A model score is not a diagnosis by itself; it becomes a decision only after applying a threshold.
- Evaluation should include sensitivity, specificity, PPV, NPV, ROC/AUC, calibration, and confidence intervals.

## Important Formulas

Prevalence means the fraction of examples that truly have the condition.

\[
\text{Prevalence} = \frac{\text{number of positive labels}}{\text{number of all labels}}
\]

Where:

- Positive labels are examples where the disease is present.
- All labels are all examples being evaluated for that disease.

Accuracy means the fraction of predictions that are correct, counting both positive and negative cases.

\[
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
\]

Where:

- \(TP\) means true positives.
- \(TN\) means true negatives.
- \(FP\) means false positives.
- \(FN\) means false negatives.

## Human-Readable Explanation

The pipeline starts by asking whether the data split is trustworthy. If the same patient appears in both training and validation data, the model may appear to perform well because it recognizes patient-specific patterns instead of learning disease evidence. After the split is trusted, images are standardized, class imbalance is handled through loss weighting, and a DenseNet-based classifier learns a probability for each disease label.

Evaluation then asks a different question: if the model produces probabilities, what happens when those probabilities are turned into decisions? A high threshold reduces false positives but can miss real disease. A low threshold catches more disease but can create more false alarms. The Week 2 metrics explain these tradeoffs.

## Key Code Patterns

Check patient overlap with set intersection:

```python
def check_for_leakage(df1, df2, patient_col="PatientId"):
    group_1 = set(df1[patient_col].unique())
    group_2 = set(df2[patient_col].unique())
    return len(group_1.intersection(group_2)) > 0
```

Turn prediction scores into binary decisions:

```python
thresholded_preds = pred >= th
```

## Common Mistakes

- Evaluating a split that has patient overlap.
- Normalizing validation or test images with statistics computed from that validation or test batch.
- Reporting accuracy alone on a rare disease task.
- Treating a model probability as a final diagnosis without selecting and justifying a threshold.
- Forgetting that PPV and NPV change when prevalence changes.

## Takeaways

The course is about disciplined medical ML practice: protect the split, handle imbalance, use transfer learning carefully, and evaluate predictions with metrics that match clinical risk.
