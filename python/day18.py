
import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "Student": ["Ali", "Sara", "Ahmed", "Ayesha", "Usman",
                "Hina", "Bilal", "Zara"],
    "StudyHours": [2, 5, 1, 6, 3, 7, 2, 5],
    "Attendance": [70, 90, 60, 95, 75, 98, 65, 88],
    "FinalScore": [55, 85, 45, 92, 65, 96, 50, 82]
}

df = pd.DataFrame(data)

# 1. Display the dataset
print("\n--- Complete Dataset ---")
print(df)

# 2. Understand dataset size
print("\n--- Dataset Shape ---")
print(df.shape)

# 3. Check column names and data types
print("\n--- Dataset Information ---")
df.info()

# 4. Calculate statistics
print("\n--- Statistical Summary ---")
print(df.describe())

# 5. Check missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# 6. Check duplicate rows
print("\n--- Duplicate Rows ---")
print(df.duplicated().sum())

# 7. Find average final score
print("\nAverage Final Score:")
print(df["FinalScore"].mean())

# 8. Find students scoring above 80
print("\n--- Students Scoring Above 80 ---")
print(df[df["FinalScore"] > 80])

# 9. Check relationship between numerical columns
print("\n--- Correlation Matrix ---")
print(df[["StudyHours", "Attendance", "FinalScore"]].corr())

# 10. Visualize study hours vs final scores
plt.figure(figsize=(7, 5))
plt.scatter(df["StudyHours"], df["FinalScore"])

plt.title("Study Hours vs Final Score")
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.grid(True)
plt.show()


# Exercise 1: Find highest and lowest final scores
print("\n--- Highest and Lowest Final Scores ---")

print("Highest score:", df["FinalScore"].max())
print("Lowest score:", df["FinalScore"].min())


# Exercise 2: Display students with attendance below 75
print("\n--- Students with Attendance Below 75% ---")

low_attendance = df[df["Attendance"] < 75]
print(low_attendance)


# Exercise 3: Scatter plot of Attendance vs FinalScore
print("\n--- Attendance vs Final Score Scatter Plot ---")

plt.figure(figsize=(7, 5))

plt.scatter(df["Attendance"], df["FinalScore"])

plt.title("Attendance vs Final Score")
plt.xlabel("Attendance (%)")
plt.ylabel("Final Score")
plt.grid(True)

plt.show()