## Project Summary: AWS Log Analytics

This project showcases a server log analytics pipeline using AWS-native services. It simulates real-world log ingestion, cleaning, transformation, and querying.

### 🔍 Objective
To build a scalable data engineering workflow using AWS services that can ingest raw server logs, process them, and analyze them using SQL queries.

### 📝 Dataset
Sample log data with columns:
- timestamp
- method
- endpoint
- status_code
- user_id

### 🔧 Steps Performed

1. Uploaded `logs_sample.csv` to S3 bucket under `raw-logs/`
2. Created AWS Glue Crawler to create schema in Glue Catalog
3. Wrote a Glue ETL job in PySpark:
   - Parsed timestamp column
   - Converted data to Parquet
   - Stored output in `processed-logs/` folder in S3
4. Used Athena to create external table and run queries

### 📊 Sample Athena Queries
- Count total log records
- Error count (status_code = 500)
- Most used endpoints
- Most error-prone users

### 💡 Real-World Use Cases
- Application monitoring
- Error trend tracking
- API usage patterns
- Dashboard backend for DevOps/Infra teams

---

✅ A fully serverless, scalable log analytics system built on top of AWS!
