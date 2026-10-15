import pandas as pd
import joblib

# 1. Load the saved model
model = joblib.load("student_model.pkl")

# 2. Create a reusable prediction function
def predict_score(study_hours, attendance, previous_marks):

    student = pd.DataFrame({
        "StudyHours": [study_hours],
        "Attendance": [attendance],
        "PreviousMarks": [previous_marks]
    })

    prediction = model.predict(student)

    return round(prediction[0], 2)


# 3. Predict scores for three students
student1 = predict_score(5, 82, 68)
student2 = predict_score(7, 90, 80)
student3 = predict_score(3, 65, 45)

print("Student 1 predicted score:", student1)
print("Student 2 predicted score:", student2)
print("Student 3 predicted score:", student3)