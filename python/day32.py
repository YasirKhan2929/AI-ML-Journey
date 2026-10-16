
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import accuracy_score

# Create the same student dataset
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

# Split the dataset once for a fair comparison
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Define the models
models = {
    "Logistic Regression": make_pipeline(
        StandardScaler(),
        LogisticRegression(random_state=42)
    ),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ),
    "KNN": make_pipeline(
        StandardScaler(),
        KNeighborsClassifier(n_neighbors=5)
    ),
    "SVM": make_pipeline(
        StandardScaler(),
        SVC(kernel="linear")
    ),
    "Naive Bayes": GaussianNB()
}

# Train and evaluate each model
print("MODEL COMPARISON")
print("-" * 45)

results = []

for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    results.append((name, accuracy))

# Display results from highest to lowest accuracy
results.sort(key=lambda item: item[1], reverse=True)

for name, accuracy in results:
    print(f"{name:<22} Accuracy: {accuracy:.2%}")
