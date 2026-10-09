import pandas as pd

df = pd.read_csv("students.csv")

print("Complete dataset:")
print(df)

print("\nFirst 3 rows:")
print(df.head(3))

print("\nDataset information:")
print(df.info())

print("\nDataset shape:")
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nAverage marks:")
print(df[["Python", "NumPy", "Pandas"]].mean())

print("\nStudents with Python marks above 80:")
print(df[df["Python"] > 80])

print("\nStudent with the highest Pandas marks:")
print(df.loc[df["Pandas"].idxmax()])

print("display last two rows: \n", df.tail(2))
print("number of students with python marks aove 75: ")
print(len(df[df["Python"]>75]))
print("\nStudent with the Lowest Numpy marks:")
print(df.loc[df["NumPy"].idxmin()])