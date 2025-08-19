# Databricks notebook source
# MAGIC %md
# MAGIC ### Data Reading

# COMMAND ----------

dbutils.fs.ls('/FileStore/tables/')

# COMMAND ----------

df = spark.read.format('csv').option('inferSchema',True).option('header',True).load('/FileStore/tables/BigMart_Sales.csv')

# COMMAND ----------

df.display()

# COMMAND ----------

# MAGIC  %md
# MAGIC ### Data Reading JSON

# COMMAND ----------

df_json = spark.read.format('json').option('inferSchema',True)\
                    .option('header',True)\
                    .option('multiLine',False)\
                    .load('/FileStore/tables/drivers.json')    
df_json.display()                    

# COMMAND ----------

# MAGIC %md
# MAGIC ### Schema

# COMMAND ----------

df.printSchema()

# COMMAND ----------

my_ddl_schema = '''
                    Item_Identifier string,
                    Item_Weight string,
                    Item_Fat_Content string,
                    Item_Visibility double,
                    Item_Type string,
                    Item_MRP double,
                    Outlet_Identifier string,
                    Outlet_Establishment_Year integer,
                    Outlet_Size string,
                    Outlet_Location_Type string,
                    Outlet_Type string,
                    Item_Outlet_Sales double
                    '''

# COMMAND ----------

df = spark.read.format('csv')\
               .schema(my_ddl_schema)\
               .option('header',True)\
               .load('/FileStore/tables/BigMart_Sales.csv')        
df.display()               

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

my_strct_schema = StructType([
                                StructField('Item_Identifier',StringType(),True),
                                StructField('Item_Weight',StringType(),True),
                                StructField('Item_Fat_Content',StringType(),True),
                                StructField('Item_Visibility',StringType(),True),
                                StructField('Item_Type',StringType(),True),
                                StructField('Item_MRP',StringType(),True),
                                StructField('Outlet_Identifier',StringType(),True),
                                StructField('Outlet_Establishment_Year',StringType(),True),
                                StructField('Outlet_Size',StringType(),True),
                                StructField('Outlet_Location_Type',StringType(),True),
                                StructField('Outlet_Type',StringType(),True),
                                StructField('Item_Outlet_Sales',StringType(),True),

])

# COMMAND ----------

df = spark.read.format('csv')\
               .schema(my_strct_schema)\
               .option('header',True)\
               .load('/FileStore/tables/BigMart_Sales.csv')  

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df.select('Item_Identifier','Item_Weight','Item_Fat_Content').display()
# df.select(col('Item_Identifier'),col('Item_Waight'),col('Item_Fat_Content')).display() -----use this as it is a standard approach


# COMMAND ----------

# MAGIC %md
# MAGIC ### ALIAS

# COMMAND ----------

df.select(col('Item_Identifier').alias('Item_ID')).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###FILTER

# COMMAND ----------

# MAGIC %md
# MAGIC #### Scenario 1 (Filter the data with fat content Regular)

# COMMAND ----------

df.display()

# COMMAND ----------

df.filter(col('Item_Fat_Content')=='Regular').display()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Scenario 2 (Slice the data with item_type=soft drinks and weight < 10)

# COMMAND ----------

df.filter((col('Item_Type')=='Soft Drinks') & (col('Item_Weight')<10)).display()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Scenario 3(Fetch the data with Tier in (Tier 1 or Tier 2)) and outlet size is null
# MAGIC

# COMMAND ----------

df.filter(col('Outlet_Location_Type').isin('Tier 1','Tier 2') & (col('Outlet_Size').isNull())).display()

# COMMAND ----------

# MAGIC %md
# MAGIC #### withColumnRenamed

# COMMAND ----------

df.withColumnRenamed('Item_Weight','Item_Wt').display()

# COMMAND ----------

# MAGIC %md
# MAGIC #### withColumn

# COMMAND ----------

df = df.withColumn('flag',lit('new'))
df.display()

# COMMAND ----------

df = df.withColumn('Item_Weight + Item_MRP',col('Item_Weight')+col('Item_MRP'))
df.display()

# COMMAND ----------

df.withColumn('Item_Fat_Content',regexp_replace(col('Item_Fat_Content'),'Regular','Reg'))\
    .withColumn('Item_Fat_Content',regexp_replace(col('Item_Fat_Content'),'Low Fat','LF')).display()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Type Casting

# COMMAND ----------

df = df.withColumn("Item_Weight",col("Item_Weight").cast('double'))
df.printSchema()

# COMMAND ----------

df.select("Item_Identifier",col("Item_MRP").cast('double').alias("Item_MRP_double")).display()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Sort

# COMMAND ----------

df.sort(col('Item_Weight').asc()).display()

# COMMAND ----------

df.sort(col('Item_Weight').desc()).display()

# COMMAND ----------

df.sort(['Item_Weight','Item_MRP'],ascending = [0.0]).display()

# COMMAND ----------

df.sort(['Item_Weight','Item_MRP'],ascending = [1,0]).display()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Limit

# COMMAND ----------

df.limit(10).display()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Drop Duplicates

# COMMAND ----------

df.dropDuplicates().display()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Scenario 2

# COMMAND ----------

df.drop_duplicates(subset= ['Item_Type']).display()

# COMMAND ----------

df.distinct().display()

# COMMAND ----------


