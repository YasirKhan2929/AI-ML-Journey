
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.pipeline import make_pipeline

# Create the same 32-record student dataset
X = []
y = []

study_hours_options = [1, 2, 3, 4, 5, 6, 7, 8]
attendance_options = [40, 55, 70, 85]

for hours in study_hours_options:
    for attendance in attendance_options:
        X.append([hours, attendance])

        if hours >= 4 and attendance >= 70:
            y.append(1)  # Pass
        else:
            y.append(0)  # Fail

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Scale features and create the KNN model
model = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=7)
)

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)

print("Training records:", len(X_train))
print("Testing records:", len(X_test))
print("Actual results:", y_test)
print("Predicted results:", predictions)
print("Accuracy:", round(accuracy_score(y_test, predictions), 2))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

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
