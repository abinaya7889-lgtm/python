import pandas as pd

data = {
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone"],
    "Quantity": [5, 10, 7, 3, 8],
    "Price": [50000, 20000, 15000, 50000, 20000]
}

df = pd.DataFrame(data)
df["Sales"] = df["Quantity"] * df["Price"]

print("Sales Dataset:")
print(df)