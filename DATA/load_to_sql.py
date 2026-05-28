import pandas as pd
import sqlite3

# Read processed CSV
df = pd.read_csv("processed_sales_orders.csv")

# Create SQLite database
conn = sqlite3.connect("sales_database.db")

# Load data into SQL table
df.to_sql("sales_orders", conn, if_exists="replace", index=False)

print("Data Loaded Successfully into SQL Database!")

# Verify data
result = pd.read_sql("SELECT * FROM sales_orders", conn)
print(result.head())

conn.close()