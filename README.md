# AWS Log Analytics Project

This project shows how to process and analyze server logs using AWS services like S3, Glue, and Athena.

## ✅ What It Does

- Stores raw log files in Amazon S3
- Uses AWS Glue Crawler to detect and catalog the data
- Runs an AWS Glue ETL job (PySpark) to clean and convert CSV to Parquet
- Stores the processed data back to S3
- Queries the data using Amazon Athena with SQL

## 🧱 Tools & Technologies

- AWS S3  
- AWS Glue (Crawler + PySpark ETL job)  
- AWS Athena  
- PySpark  
- CSV and Parquet

## 📊 Example Use Cases

- Count number of error logs (like 500 status code)
- Find most accessed API endpoints
- Track which users triggered the most failures


## 📁 Project Files

- `logs_sample.csv` – Sample server log file
- `glue_etl_script.py` – PySpark script for Glue job
- `athena_queries.sql` – SQL queries run in Athena
- `project_summary.md` – Detailed explanation of the project
- `screenshots/` – Images showing S3, Glue, and Athena steps

