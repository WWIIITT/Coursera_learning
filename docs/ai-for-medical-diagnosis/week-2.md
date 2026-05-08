# Week 2 - Diagnostic Model Evaluation

## What This Covers

Week 2 evaluates diagnostic models after they produce prediction scores. It covers thresholded predictions, confusion-matrix counts, accuracy, prevalence, sensitivity, specificity, PPV, NPV, ROC/AUC, confidence intervals, precision-recall curves, F1 score, and calibration.

## Core Ideas

- A model usually outputs probabilities; a threshold turns those probabilities into positive or negative predictions.
- The confusion matrix separates correct positives, correct negatives, false alarms, and missed cases.
- Accuracy can be misleading when disease prevalence is low.
- Sensitivity and specificity describe model behavior conditioned on the true disease state.
- PPV and NPV describe what a prediction means after the model has made it.
- ROC and PR curves show how metrics change across thresholds.
- Calibration checks whether predicted probabilities match observed frequencies.

## Important Formulas

True positives are actually positive cases predicted as positive.

\[
TP = \sum \mathbf{1}(y = 1 \text{ and } \hat{y}_{\text{binary}} = 1)
\]

True negatives are actually negative cases predicted as negative.

\[
TN = \sum \mathbf{1}(y = 0 \text{ and } \hat{y}_{\text{binary}} = 0)
\]

False positives are actually negative cases predicted as positive.

\[
FP = \sum \mathbf{1}(y = 0 \text{ and } \hat{y}_{\text{binary}} = 1)
\]

False negatives are actually positive cases predicted as negative.

\[
FN = \sum \mathbf{1}(y = 1 \text{ and } \hat{y}_{\text{binary}} = 0)
\]

Where:

- \(y\) is the true label.
- \(\hat{y}_{\text{binary}}\) is the thresholded prediction.
- \(\mathbf{1}(\cdot)\) means count 1 when the condition is true.

Accuracy means the fraction of all predictions that are correct.

\[
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
\]

Prevalence means how common the condition is in the evaluated population.

\[
\text{Prevalence} = \frac{TP + FN}{TP + TN + FP + FN}
\]

Sensitivity means: among truly positive cases, the fraction correctly predicted positive.

\[
\text{Sensitivity} = \frac{TP}{TP + FN}
\]

Specificity means: among truly negative cases, the fraction correctly predicted negative.

\[
\text{Specificity} = \frac{TN}{TN + FP}
\]

Positive predictive value means: among positive predictions, the fraction that are truly positive.

\[
PPV = \frac{TP}{TP + FP}
\]

Negative predictive value means: among negative predictions, the fraction that are truly negative.

\[
NPV = \frac{TN}{TN + FN}
\]

F1 score means the harmonic mean of precision and recall.

\[
F1 = \frac{2 \times \text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
\]

Where:

- Precision is the same idea as PPV.
- Recall is the same idea as sensitivity.

## Human-Readable Explanation

Thresholds control the tradeoff between missed disease and false alarms. If the threshold is high, the model requires strong evidence before predicting disease, which usually increases specificity and lowers sensitivity. If the threshold is low, the model catches more true disease but may create more false positives.

Sensitivity and specificity answer questions from the ground-truth perspective. Sensitivity asks how often the model catches disease when disease is really present. Specificity asks how often the model stays quiet when disease is really absent.

PPV and NPV answer questions from the prediction perspective. PPV asks how much trust to place in a positive prediction. NPV asks how much trust to place in a negative prediction. These values depend strongly on prevalence, so they can change when the same model is used in a different population.

ROC curves plot sensitivity against false positive rate over many thresholds. AUC summarizes the model's ranking ability. Precision-recall curves are often more informative for rare diseases because they focus on positive predictions.

Calibration is different from discrimination. A model can rank patients well but still assign probabilities that are too high or too low. A calibrated model's predicted probabilities should match real observed frequencies.

## Key Code Patterns

Compute confusion-matrix counts:

```python
thresholded_preds = pred >= th
TP = np.sum((y == 1) & (thresholded_preds == 1))
TN = np.sum((y == 0) & (thresholded_preds == 0))
FP = np.sum((y == 0) & (thresholded_preds == 1))
FN = np.sum((y == 1) & (thresholded_preds == 0))
```

Compute the Week 2 metrics:

```python
accuracy = (TP + TN) / (TP + TN + FP + FN)
prevalence = np.mean(y)
sensitivity = TP / (TP + FN)
specificity = TN / (TN + FP)
ppv = TP / (TP + FP)
npv = TN / (TN + FN)
```

Bootstrap confidence intervals by repeatedly sampling positives and negatives, computing a statistic each time, and taking percentiles of the bootstrap distribution.

## Common Mistakes

- Treating AUC as proof that the chosen threshold is clinically acceptable.
- Comparing PPV across datasets without checking prevalence.
- Optimizing for accuracy on imbalanced disease labels.
- Calling a model well calibrated because it has a good ROC curve.
- Forgetting that a false negative may be more costly than a false positive for some diseases.

## Takeaways

Week 2 turns model output into clinical interpretation. Good evaluation explains what the model catches, what it misses, how much predictions can be trusted, and how those answers change with threshold and prevalence.
