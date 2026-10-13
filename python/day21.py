
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Create a sample dataset
data = {
    "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "FinalScore": [35, 40, 50, 55, 65, 70, 75, 85, 90, 95]
}

df = pd.DataFrame(data)

print("--- Dataset ---")
print(df)

# 2. Separate inputs (X) and target (y)
X = df[["StudyHours"]]
y = df["FinalScore"]

# 3. Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# 4. Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Predict scores for the test data
predictions = model.predict(X_test)

print("\n--- Actual vs Predicted Scores ---")
results = pd.DataFrame({
    "StudyHours": X_test["StudyHours"].values,
    "ActualScore": y_test.values,
    "PredictedScore": predictions.round(2)
})
print(results.sort_values("StudyHours"))

# 6. Evaluate the model
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nMean Absolute Error:", round(mae, 2))
print("R² Score:", round(r2, 2))

# 7. Predict for a new example
new_student = pd.DataFrame({"StudyHours": [4.5]})
predicted_score = model.predict(new_student)

print("\nPredicted score for 4.5 study hours:",
      round(predicted_score[0], 2))
