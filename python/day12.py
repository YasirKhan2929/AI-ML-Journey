import pandas as pd
import numpy as np

data = {
    "Student": ["Ali", "Sara", "Ahmed", "Ayesha"],
    "Python": [78, 90, 65, 82],
    "NumPy": [85, 95, 72, 79],
    "Pandas": [92, 93, 68, 85]
}

df = pd.DataFrame(data)

print(df)

# print("\nDataset shape:")
# print(df.shape)

# print("\nColumn names:")
# print(df.columns)

# print("\nStudent names:")
# print(df["Student"])

# print("\nPython marks:")
# print(df["Python"])

# print("\nFirst two rows:")
# print(df.head(2))

# print("\nSara's record:")
# print(df[df["Student"] == "Sara"])

# print('\nNumpy column')
# print(df["NumPy"])
# print('Last two rows')
# print(df.tail(2))

# #finding student whose python marks greater than 80
# st = df[df["Python"]>80]
# print(st)
print("\nAverage Python marks:")
print(df["Python"].mean())

print("\nAverage marks in each subject:")
print(df[["Python", "NumPy", "Pandas"]].mean())

print("\nHighest marks in each subject:")
print(df[["Python", "NumPy", "Pandas"]].max())

print("\nLowest marks in each subject:")
print(df[["Python", "NumPy", "Pandas"]].min())

print("\nDataset summary:")
print(df.describe())

print("average of numpy: ")
print(df["NumPy"].mean())

#finding studend with highest pandas marks
top_student = df.loc[df["Pandas"].idxmax()]
print("Top student:", top_student["Student"])
print("Highest Pandas marks:", top_student["Pandas"])

st = df[df["NumPy"]>80]
print(st)

print("average of all students: ")
students_avg = df[["NumPy", "Pandas", "Python"]].mean(axis=1)
print(students_avg)
print(f"Average of students who secure more than 80 marks: ",students_avg[students_avg>80])
result = df[students_avg > 80]
print(result[["Student"]])
print(students_avg[students_avg > 80])