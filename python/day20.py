
import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Usman", "Hina"],
    "StudyHours": [2, 5, 1, 6, 3, 7],
    "Attendance": [70, 90, 60, 95, 75, 98],
    "FinalScore": [55, 85, 45, 92, 65, 96]
}

df = pd.DataFrame(data)

print("\n--- Original Dataset ---")
print(df)

# 1. Create a new feature: Study hours category
df["StudyLevel"] = df["StudyHours"].apply(
    lambda hours: "High" if hours >= 5 else "Low"
)

print("\n--- Study Level Feature ---")
print(df[["Name", "StudyHours", "StudyLevel"]])

# 2. Create a new feature: Attendance category
df["AttendanceLevel"] = df["Attendance"].apply(
    lambda attendance: "Good" if attendance >= 80 else "Low"
)

print("\n--- Attendance Level Feature ---")
print(df[["Name", "Attendance", "AttendanceLevel"]])

# 3. Create a performance category from final score
df["PerformanceCategory"] = pd.cut(
    df["FinalScore"],
    bins=[0, 50, 80, 100],
    labels=["Needs Improvement", "Average", "Excellent"],
    include_lowest=True
)

print("\n--- Performance Category ---")
print(df[["Name", "FinalScore", "PerformanceCategory"]])

# 4. Calculate study hours per attendance point
df["StudyAttendanceRatio"] = df["StudyHours"] / df["Attendance"]

print("\n--- Final Dataset with New Features ---")
print(df)

# 5. Save the engineered dataset
df.to_csv("engineered_students.csv", index=False)

print("\nDataset saved as engineered_students.csv")

df["StudyCategory"] = df["StudyHours"].apply(
    lambda hours: (
        "Beginner" if hours < 3
        else "Intermediate" if hours <= 5
        else "Advanced"
    )
)

print("\n--- Study Categories ---")
print(df[["Name", "StudyHours", "StudyCategory"]])

df["Passed"] = df["FinalScore"] >= 50

print("\n--- Pass Status ---")
print(df[["Name", "FinalScore", "Passed"]])

average_scores = df.groupby("StudyLevel")["FinalScore"].mean()

print("\n--- Average Final Score by Study Level ---")
print(average_scores)

df.to_csv("engineered_students.csv", index=False)
print("\nUpdated dataset saved successfully!")
