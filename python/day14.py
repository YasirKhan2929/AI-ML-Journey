import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ali", "Ayesha"],
    "Age": [22, 24, None, 22, 23],
    "Salary": [50000, 65000, 45000, 50000, None],
    "Department": ["IT", "HR", "IT", "IT", "Finance"]
}

df = pd.DataFrame(data)

print("Original dataset:")
print(df)



print("\nFill missing Age with the average:")
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df)

print("\nFill missing Salary with the average:")
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df)
df = df.drop_duplicates()

print("\nDataset after removing duplicates:")
print(df)
print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())