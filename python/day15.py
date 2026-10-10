import pandas as pd

data = {
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone", "Tablet"],
    "Region": ["North", "South", "North", "South", "North", "South"],
    "Sales": [80000, 50000, 30000, 90000, 60000, 35000],
    "Quantity": [2, 5, 3, 3, 6, 4]
}

df = pd.DataFrame(data)

print("Original dataset:")
print(df)

print("\nSales from highest to lowest:")
print(df.sort_values(by="Sales", ascending=False))

print("\nTotal sales by product:")
print(df.groupby("Product")["Sales"].sum())

print("\nAverage sales by region:")
print(df.groupby("Region")["Sales"].mean())