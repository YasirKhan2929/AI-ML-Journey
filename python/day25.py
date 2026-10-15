
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Create a labeled dataset
data = {
    "StudyHours": [
        1, 2, 2, 3, 3, 4, 4, 5, 5, 6,
        6, 7, 7, 8, 8, 9, 2, 4, 6, 9
    ],
    "Attendance": [
        30, 40, 45, 50, 55, 60, 65, 70, 75, 80,
        82, 85, 88, 90, 92, 95, 35, 55, 78, 98
    ],
    "Result": [
        "Fail", "Fail", "Fail", "Fail", "Fail",
        "Fail", "Fail", "Pass", "Pass", "Pass",
        "Pass", "Pass", "Pass", "Pass", "Pass", "Pass",
        "Fail", "Fail", "Pass", "Pass"
    ]
}

df = pd.DataFrame(data)

# 2. Separate features and target
X = df[["StudyHours", "Attendance"]]
y = df["Result"]

# 3. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

print("Training records:", len(X_train))
print("Testing records:", len(X_test))

# 4. Train the classification model
model = LogisticRegression()
model.fit(X_train, y_train)

print("Model trained successfully!")

# 5. Evaluate on test data
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Actual categories:", list(y_test))
print("Predicted categories:", list(y_pred))
print("Accuracy:", round(accuracy * 100, 2), "%")

# 6. Predict for a new student
new_student = pd.DataFrame({
    "StudyHours": [5],
    "Attendance": [75]
})

prediction = model.predict(new_student)

print("New student's predicted result:", prediction[0])
