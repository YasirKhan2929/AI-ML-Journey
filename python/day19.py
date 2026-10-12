
import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ali", "Ayesha", "Usman"],
    "Age": [22, 24, None, 22, 150, 23],
    "StudyHours": [2, 5, 3, 2, -1, None],
    "FinalScore": [55, 85, 45, 55, 92, 110]
}

df = pd.DataFrame(data)

print("\n--- Original Dataset ---")
print(df)

# Exercise 1: Count rows before and after removing duplicates
rows_before = len(df)
df = df.drop_duplicates()
rows_after = len(df)

print("\n--- Duplicate Removal ---")
print("Rows before removing duplicates:", rows_before)
print("Rows after removing duplicates:", rows_after)
print("Duplicate rows removed:", rows_before - rows_after)

# Replace invalid values with missing values
df.loc[(df["Age"] < 5) | (df["Age"] > 100), "Age"] = None
df.loc[df["StudyHours"] < 0, "StudyHours"] = None
df.loc[(df["FinalScore"] < 0) | (df["FinalScore"] > 100), "FinalScore"] = None

# Fill missing numeric values with median
for column in ["Age", "StudyHours", "FinalScore"]:
    df[column] = df[column].fillna(df[column].median())

print("\n--- Cleaned Dataset ---")
print(df)

# Exercise 2: Display students with FinalScore greater than 80
print("\n--- Students Scoring Above 80 ---")
high_scorers = df[df["FinalScore"] > 80]
print(high_scorers)

# Exercise 3: Save cleaned data to CSV
df.to_csv("cleaned_students.csv", index=False)

print("\nCleaned dataset saved to cleaned_students.csv")
