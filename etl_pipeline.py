import pandas as pd

# Extract
df = pd.read_csv("data/sales_orders.csv")

# Transform
df["TotalAmount"] = df["Quantity"] * df["Price"]

# Load
df.to_csv("processed_sales_orders.csv", index=False)

# Output
print("ETL Pipeline Executed Successfully!")
print(df.head())