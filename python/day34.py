from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Create student data
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

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Model A: Unrestricted Decision Tree
deep_tree = DecisionTreeClassifier(random_state=42)
deep_tree.fit(X_train, y_train)

# Model B: Decision Tree limited to depth 2
small_tree = DecisionTreeClassifier(
    max_depth=2,
    random_state=42
)
small_tree.fit(X_train, y_train)

# Compare performance
models = {
    "Unrestricted Tree": deep_tree,
    "Depth-2 Tree": small_tree
}

print("OVERFITTING EXPERIMENT")
print("-" * 40)

for name, model in models.items():
    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)

    train_accuracy = accuracy_score(
        y_train, train_predictions
    )
    test_accuracy = accuracy_score(
        y_test, test_predictions
    )

    print(f"\n{name}")
    print(f"Training accuracy: {train_accuracy:.2%}")
    print(f"Testing accuracy:  {test_accuracy:.2%}")
