# Configure Spark Logging in Databricks
# This shows how to use the log4j.properties file with PySpark in Databricks

from pyspark.sql import SparkSession
import os

# Define path to log4j.properties (in Databricks, you'd typically upload this to DBFS)
# For local testing, use a relative or absolute path
log4j_path = "log4j.properties"  # For Databricks: "/dbfs/FileStore/config/log4j.properties"

# Create a SparkSession with logging configuration
spark = (SparkSession.builder
    .appName("LoggingExample")
    .config("spark.driver.extraJavaOptions", f"-Dlog4j.configuration=file:{log4j_path}")
    .config("spark.executor.extraJavaOptions", f"-Dlog4j.configuration=file:{log4j_path}")
    # Optional: Set log level dynamically
    .config("spark.log.level", "INFO")  
    .getOrCreate())

# Get Spark logger
log4j = spark._jvm.org.apache.log4j
logger = log4j.LogManager.getLogger("LoggingExample")

# Log some messages
logger.info("This is an INFO message")
logger.warn("This is a WARNING message")
logger.error("This is an ERROR message")

# Your PySpark code here
data = [("Alice", 1), ("Bob", 2), ("Charlie", 3)]
df = spark.createDataFrame(data, ["Name", "ID"])
logger.info(f"DataFrame created with {df.count()} rows")
df.show()

# In Databricks, you can also access logs through the Spark UI or in DBFS at the configured path
print("Check logs in the Spark UI or in DBFS at the configured path")
