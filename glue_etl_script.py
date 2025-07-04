import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, to_timestamp
from awsglue.dynamicframe import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Load from Glue Catalog
datasource = glueContext.create_dynamic_frame.from_catalog(
    database="logdb", table_name="raw_logs"
)

# Convert to DataFrame
df = datasource.toDF()

# Convert timestamp string to actual timestamp
df_clean = df.withColumn("timestamp", to_timestamp("timestamp", "yyyy-MM-dd HH:mm:ss"))

# Convert back to DynamicFrame
final_dyf = DynamicFrame.fromDF(df_clean, glueContext, "final_dyf")

# Write to S3 as Parquet
glueContext.write_dynamic_frame.from_options(
    frame=final_dyf,
    connection_type="s3",
    connection_options={"path": "s3://your-bucket-name/processed-logs/"},
    format="parquet"
)

job.commit()
