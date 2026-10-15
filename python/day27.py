
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Create a larger synthetic student dataset
X = []
y = []

study_hours_options = [1, 2, 3, 4, 5, 6, 7, 8]
attendance_options = [40, 55, 70, 85]

for hours in study_hours_options:
    for attendance in attendance_options:
        X.append([hours, attendance])

        # Practice rule for generating labels:
        # Pass if study hours >= 4 AND attendance >= 70
        if hours >= 4 and attendance >= 70:
            y.append(1)  # Pass
        else:
            y.append(0)  # Fail

print("Total student records:", len(X))

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Train the Decision Tree
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)

print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))
print("Actual results:", y_test)
print("Predicted results:", predictions)
print("Accuracy:", round(accuracy_score(y_test, predictions), 2))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

# Display the rules learned by the model
rules = export_text(
    model,
    feature_names=["StudyHours", "Attendance"]
)

print("\nLearned Decision Tree Rules:")
print(rules)

# Predict for three new students
new_students = [
    [2, 85],
    [5, 60],
    [6, 90],
    [4, 70]
]

new_predictions = model.predict(new_students)

print("\nNew Student Predictions:")
for student, prediction in zip(new_students, new_predictions):
    result = "Pass" if prediction == 1 else "Fail"
    print(
        f"Study Hours: {student[0]}, "
        f"Attendance: {student[1]}% -> {result}"
    )
# print("\nAll Student Records:")
# print("StudyHours | Attendance | Result")

# for i in range(len(X)):
#     result = "Pass" if y[i] == 1 else "Fail"

#     print(f"{X[i][0]:10} | {X[i][1]:10}% | {result}")