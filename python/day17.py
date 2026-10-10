import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [120, 150, 135, 180, 200, 175],
    "Expenses": [80, 90, 85, 110, 130, 115]
}

df = pd.DataFrame(data)

print("Complete dataset:")
print(df)

print("\nDataset summary:")
print(df.describe())

# # Line chart
# plt.figure()
# plt.plot(df["Month"], df["Sales"], marker="o")
# plt.title("Monthly Sales")
# plt.xlabel("Month")
# plt.ylabel("Sales")

# # Bar chart
# plt.figure()
# plt.bar(df["Month"], df["Sales"], label="Sales")
# plt.bar(df["Month"], df["Expenses"], label="Expenses")
# plt.title("Monthly Sales vs Expenses")
# plt.xlabel("Month")
# plt.ylabel("Amount")
# plt.legend()

# # Display both figures
# plt.show()

# Create two side-by-side plots
# fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# # Line chart
# axes[0].plot(df["Month"], df["Sales"], marker="o")
# axes[0].set_title("Monthly Sales")
# axes[0].set_xlabel("Month")
# axes[0].set_ylabel("Sales")

# # Bar chart
# axes[1].bar(df["Month"], df["Sales"], label="Sales")
# axes[1].bar(df["Month"], df["Expenses"], label="Expenses")
# axes[1].set_title("Monthly Sales vs Expenses")
# axes[1].set_xlabel("Month")
# axes[1].set_ylabel("Amount")
# axes[1].legend()

# plt.tight_layout()
# plt.show()

import numpy as np

x = np.arange(len(df["Month"]))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(x - width/2, df["Sales"], width, label="Sales")
ax.bar(x + width/2, df["Expenses"], width, label="Expenses")

ax.set_title("Monthly Sales vs Expenses")
ax.set_xlabel("Month")
ax.set_ylabel("Amount")
ax.set_xticks(x)
ax.set_xticklabels(df["Month"])
ax.legend()

plt.tight_layout()
plt.show()