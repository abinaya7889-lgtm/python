import pandas as pd

data = {
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone"],
    "Sales": [250000, 300000, 120000, 150000, 180000]
}

df = pd.DataFrame(data)

result = df.groupby("Product")["Sales"].sum()

best_product = result.idxmax()
highest_sales = result.max()

print("Best-Selling Product:", best_product)
print("Total Sales:", highest_sales)