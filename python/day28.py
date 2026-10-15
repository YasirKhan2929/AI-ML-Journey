
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.tree import export_text

# Create the same 32-record dataset from Day 27
X = []
y = []

study_hours_options = [1, 2, 3, 4, 5, 6, 7, 8]
attendance_options = [40, 55, 70, 85]

for hours in study_hours_options:
    for attendance in attendance_options:
        X.append([hours, attendance])

        # Practice rule: Pass if both conditions are met
        if hours >= 4 and attendance >= 70:
            y.append(1)  # Pass
        else:
            y.append(0)  # Fail

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Create and train the Random Forest
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)

print("Training records:", len(X_train))
print("Testing records:", len(X_test))
print("Actual results:", y_test)
print("Predicted results:", predictions)

accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", round(accuracy, 2))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

# Check which features are important to the model
print("\nFeature Importance:")
print("StudyHours:", round(model.feature_importances_[0], 3))
print("Attendance:", round(model.feature_importances_[1], 3))

# Predict for new students
new_students = [
    [3, 90],
    [5, 80],
    [7, 55],
    [8, 85]
]

new_predictions = model.predict(new_students)

print("\nNew Student Predictions:")

for student, prediction in zip(new_students, new_predictions):
    result = "Pass" if prediction == 1 else "Fail"
    print(
        f"Study Hours: {student[0]}, "
        f"Attendance: {student[1]}% -> {result}"
    )
