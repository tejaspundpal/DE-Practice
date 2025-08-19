# Databricks notebook source
# MAGIC %md
# MAGIC # Configuring log4j for PySpark in Databricks
# MAGIC
# MAGIC This notebook demonstrates how to set up and use the enhanced log4j configuration in Databricks.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 1: Upload log4j.properties to DBFS
# MAGIC
# MAGIC First, upload the log4j.properties file to a location in DBFS:
# MAGIC
# MAGIC 1. In the Databricks UI, click on "Data" in the left sidebar
# MAGIC 2. Click "DBFS" and navigate to where you want to store your config (e.g., /FileStore/config/)
# MAGIC 3. Click "Upload" and select your log4j.properties file
# MAGIC
# MAGIC Alternatively, you can use the following command to upload directly:

# COMMAND ----------

# MAGIC %sh
# MAGIC # Upload log4j.properties from local driver node (if you have it there)
# MAGIC # Replace with your actual path if needed
# MAGIC mkdir -p /dbfs/FileStore/config
# MAGIC cp /tmp/log4j.properties /dbfs/FileStore/config/log4j.properties

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2: Configure Spark Session with log4j Properties
# MAGIC
# MAGIC Here's how to configure your SparkSession to use the log4j properties:

# COMMAND ----------

from pyspark.sql import SparkSession
import os

# Path to log4j.properties in DBFS
log4j_path = "/dbfs/FileStore/config/log4j.properties"

# If using a new SparkSession (note: in Databricks you typically use the existing session)
# spark = (SparkSession.builder
#     .appName("LoggingExample")
#     .config("spark.driver.extraJavaOptions", f"-Dlog4j.configuration=file:{log4j_path}")
#     .config("spark.executor.extraJavaOptions", f"-Dlog4j.configuration=file:{log4j_path}")
#     .getOrCreate())

# For the existing Databricks spark session, set log level
spark.sparkContext.setLogLevel("INFO")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3: Using the Logger in your PySpark Code
# MAGIC
# MAGIC Now you can use the configured logger in your code:

# COMMAND ----------

# Access the Java virtual machine and log4j logger
log4j = spark._jvm.org.apache.log4j
logger = log4j.LogManager.getLogger("MyDatabricksApp")

# Log messages at different levels
logger.info("This is an INFO message")
logger.warn("This is a WARNING message")
logger.error("This is an ERROR message")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Example: Logging during DataFrame operations

# COMMAND ----------

# Create sample data
data = [("Alice", 1), ("Bob", 2), ("Charlie", 3)]
df = spark.createDataFrame(data, ["Name", "ID"])

# Log before operation
logger.info(f"Processing DataFrame with initial {df.count()} rows")

# Perform some operations
filtered_df = df.filter(df.ID > 1)

# Log after operation
logger.info(f"Filtered DataFrame now has {filtered_df.count()} rows")
filtered_df.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Viewing Logs
# MAGIC
# MAGIC You can view logs in the following ways:
# MAGIC
# MAGIC 1. Spark UI - Click on "Spark UI" in your cluster or job page
# MAGIC 2. Cluster Logs - Click on "Spark UI" > "Executors" tab > "stdout" or "stderr" links
# MAGIC 3. DBFS - Check the log file location configured in your log4j.properties:

# COMMAND ----------

# MAGIC %fs ls /dbfs/logs/spark/

# COMMAND ----------

# MAGIC %md
# MAGIC ## Setting MDC Context for Tracking
# MAGIC
# MAGIC For advanced logging, you can set the Mapped Diagnostic Context (MDC) to include tracking information:

# COMMAND ----------

# Set MDC context values for logging (will appear in log entries with %X{key} in pattern)
log4j.MDC.put("userIdentifier", spark.sparkContext.sparkUser())
log4j.MDC.put("notebookId", dbutils.notebook.entry_point.getDbId())
log4j.MDC.put("jobId", spark.conf.get("spark.databricks.job.id", "interactive"))

logger.info("This log message includes MDC context information")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Best Practices
# MAGIC
# MAGIC 1. Use appropriate log levels (DEBUG, INFO, WARN, ERROR)
# MAGIC 2. Add context to log messages
# MAGIC 3. Consider using structured logging for machine parsing
# MAGIC 4. Rotate logs to manage storage
# MAGIC 5. Monitor log directories and clean up old logs
