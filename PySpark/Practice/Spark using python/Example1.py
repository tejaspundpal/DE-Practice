# Databricks notebook source
# MAGIC %md
# MAGIC ###Udemy Spark using Python

# COMMAND ----------

df = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/FileStore/tables/Warehouse_and_Retail_Sales.csv")
# df.limit(10).show()
df.limit(10).display()

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *
resulted_df = df.select('ITEM TYPE','RETAIL SALES') \
                .groupBy('ITEM TYPE') \
                .agg(avg('RETAIL SALES').alias('AVG RETAIL SALES')) \
                .sort('ITEM TYPE')
resulted_df.display()                        

# COMMAND ----------

import pyspark.pandas as ps
import matplotlib.pyplot as plt

# Convert to pandas-on-Spark DataFrame
pdf = resulted_df.pandas_api()
pdf = pdf.reset_index()
# Plot the bar chart
pdf.plot(x='ITEM TYPE', y='AVG RETAIL SALES')
plt.xlabel('Item type')
plt.ylabel('Average Retail Sales')
plt.title('Average Retail Sales by Item Type')
plt.show()

# COMMAND ----------

fire_df = spark.read.format('csv').option('header','true').option('inferSchema','true').load('/databricks-datasets/learning-spark-v2/sf-fire/sf-fire-calls.csv')
# fire_df = spark.read.csv('/databricks-datasets/learning-spark-v2/sf-fire/sf-fire-calls.csv',header='true',inferSchema='true')
fire_df.limit(10).display()

# COMMAND ----------

fire_df.createGlobalTempView('fire_service_calls_view')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM global_temp.fire_service_calls_view limit 10

# COMMAND ----------

display(_sqldf)

# COMMAND ----------

fire_df.write.saveAsTable('demo_db.fire_service_calls_tbl')

# COMMAND ----------

fire_df.columns

# COMMAND ----------

for col_name in fire_df.columns:
    fire_df = fire_df.withColumnRenamed(col_name,col_name.replace(' ','_').replace('(','').replace(')',''))

fire_df.write.format('delta').mode('append').saveAsTable('demo_db.fire_service_calls_tbl')

# COMMAND ----------

fire_df.columns

# COMMAND ----------


