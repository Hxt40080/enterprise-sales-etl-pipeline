# Enterprise Sales ETL Pipeline

## Overview
This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using Python, Pandas, and SQLite.

The pipeline:
1. Extracts sales order data from a CSV file
2. Transforms the data by calculating total sales amount
3. Loads the processed data into a SQLite database

---

## Technologies Used
- Python
- Pandas
- SQLite
- Git & GitHub
- VS Code

---

## Project Structure

enterprise-sales-etl-pipeline/
│
├── data/
│   ├── sales_orders.csv
│   └── load_to_sql.py
│
├── etl_pipeline.py
├── processed_sales_orders.csv
├── sales_database.db
├── README.md

---

## ETL Process

### Extract
Reads raw sales data from CSV.

### Transform
Calculates TotalAmount using:

TotalAmount = Quantity × Price

### Load
Loads transformed data into SQLite database.

---

## How to Run

### Run ETL Pipeline
```bash
python etl_pipeline.py