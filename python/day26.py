
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

# 1 = Pass, 0 = Fail
actual =    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
predicted = [1, 1, 1, 1, 0, 1, 1, 0, 0, 0]

# 1. Confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(actual, predicted, labels=[1, 0]))

# 2. Evaluation metrics
print("Accuracy:", round(accuracy_score(actual, predicted), 3))

print("Precision:", round(
    precision_score(actual, predicted, pos_label=1), 3
))

print("Recall:", round(
    recall_score(actual, predicted, pos_label=1), 3
))

print("F1-score:", round(
    f1_score(actual, predicted, pos_label=1), 3
))
