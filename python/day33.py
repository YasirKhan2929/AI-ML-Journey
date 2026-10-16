
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Create our practice dataset
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

# Create the KNN pipeline
pipeline = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier()
)

# Test different values of k
parameters = {
    "kneighborsclassifier__n_neighbors": [3, 5, 7, 9]
}

# Find the best setting using cross-validation
search = GridSearchCV(
    pipeline,
    parameters,
    cv=5,
    scoring="accuracy"
)

search.fit(X_train, y_train)

# Evaluate the best model on the test data
best_model = search.best_estimator_
predictions = best_model.predict(X_test)

print("HYPERPARAMETER TUNING")
print("-" * 35)
print("Best settings:", search.best_params_)
print("Best cross-validation accuracy:", round(search.best_score_, 2))
print("Test accuracy:", round(accuracy_score(y_test, predictions), 2))
