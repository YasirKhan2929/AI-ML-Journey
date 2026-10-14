
import pandas as pd
import joblib

from sklearn.linear_model import LinearRegression

# 1. Create a sample dataset
data = {
    "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Attendance": [60, 65, 70, 75, 80, 85, 90, 95],
    "PreviousMarks": [40, 45, 50, 55, 65, 70, 80, 85],
    "FinalScore": [42, 48, 55, 61, 72, 78, 88, 94]
}

df = pd.DataFrame(data)

# 2. Select input features and target
X = df[["StudyHours", "Attendance", "PreviousMarks"]]
y = df["FinalScore"]

# 3. Train the model
model = LinearRegression()
model.fit(X, y)

print("Model trained successfully!")

# 4. Save the trained model
joblib.dump(model, "student_model.pkl")

print("Model saved as student_model.pkl")

# 5. Load the saved model
loaded_model = joblib.load("student_model.pkl")

print("Model loaded successfully!")

# 6. Predict for a new student
new_student = pd.DataFrame({
    "StudyHours": [5],
    "Attendance": [82],
    "PreviousMarks": [68]
})

prediction = loaded_model.predict(new_student)

print("Predicted final score:", round(prediction[0], 2))
