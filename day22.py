
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Create a sample dataset
data = {
    "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8, 2, 6, 4, 9],
    "Attendance": [60, 65, 70, 75, 80, 85, 90, 95, 70, 88, 78, 96],
    "PreviousMarks": [40, 45, 50, 55, 65, 70, 80, 85, 48, 75, 60, 90],
    "FinalScore": [42, 48, 55, 61, 72, 78, 88, 94, 50, 84, 66, 97]
}

df = pd.DataFrame(data)

print("--- Student Dataset ---")
print(df)

# 2. Select input features and target
X = df[["StudyHours", "Attendance", "PreviousMarks"]]
y = df["FinalScore"]

# 3. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# 4. Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Predict scores for the test data
predictions = model.predict(X_test)

results = pd.DataFrame({
    "ActualScore": y_test.values,
    "PredictedScore": predictions.round(2)
})

print("\n--- Actual vs Predicted Scores ---")
print(results)

# 6. Evaluate the model
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nMean Absolute Error:", round(mae, 2))
print("R² Score:", round(r2, 2))

# 7. Predict for a new student
new_student = pd.DataFrame({
    "StudyHours": [5],
    "Attendance": [82],
    "PreviousMarks": [68]
})

predicted_score = model.predict(new_student)

print("\nPredicted final score:", round(predicted_score[0], 2))
