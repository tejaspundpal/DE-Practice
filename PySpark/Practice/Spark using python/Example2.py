# Databricks notebook source
fire_df = spark.read.format('csv').option('header','true').option('inferSchema','true').load('/databricks-datasets/learning-spark-v2/sf-fire/sf-fire-calls.csv')
# fire_df = spark.read.csv('/databricks-datasets/learning-spark-v2/sf-fire/sf-fire-calls.csv',header='true',inferSchema='true')
fire_df.limit(10).display()

# COMMAND ----------

for col_name in fire_df.columns:
    fire_df = fire_df.withColumnRenamed(col_name,col_name.replace(' ','').replace('(','').replace(')',''))
fire_df.limit(10).display()    

# COMMAND ----------

# from pyspark.sql.functions import *
# from pyspark.sql.types import *

# date_patterns = ["yyyy-MM-dd", "MM/dd/yyyy", "dd-MM-yyyy", "yyyy/MM/dd"]

# def convert_string_dates(df):
#     for column in df.columns:
#         if isinstance(df.schema[column].dataType, StringType):
#             for pattern in date_patterns:
#                 try:
#                     df = df.withColumn(column, to_date(col(column), pattern))
#                     if df.select(column).filter(col(column).isNotNull()).count() > 0:
#                         break
#                 except:
#                     continue
#     return df

# fire_df = convert_string_dates(fire_df)
# fire_df.limit(10).display(10) 

# COMMAND ----------


from pyspark.sql.functions import to_date, to_timestamp
from pyspark.sql.types import *

fire_df = fire_df.withColumn('CallDate', to_date('CallDate', 'MM/dd/yyyy')).withColumn('AvailableDtTm', to_timestamp('AvailableDtTm', 'MM/dd/yyyy hh:mm:ss a')).withColumn('WatchDate', to_date('WatchDate', 'MM/dd/yyyy'))


# COMMAND ----------

fire_df.printSchema()

# COMMAND ----------

fire_df = fire_df.withColumn('Delay',round('Delay',2))

# COMMAND ----------

fire_df.printSchema()

# COMMAND ----------

fire_df.createOrReplaceTempView('fire_df_view')
ql_sql_df = spark.sql("""
                      select count(distinct CallType) as distinct_calltype 
                      from fire_df_view where CallType is not null""")
ql_sql_df.limit(10).display()                      

# COMMAND ----------

q1_df = fire_df.where("CallType is not null")\
                .select("CallType")\
                .distinct()
display(q1_df.count())                

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

q1_df = fire_df.where("CallType is not null")\
                .select(expr("CallType as distinct_call_type"))\
                .distinct()
display(q1_df)  

# COMMAND ----------

sql_2 = spark.sql("""
                  SELECT * FROM fire_df_view WHERE Delay > 5 LIMIT 10""")
sql_2.display()                  

# COMMAND ----------

q2_df = fire_df.where("Delay > 5")\
                .select("CallNumber","Delay")
q2_df.limit(10).display()                

# COMMAND ----------

sql_3 = spark.sql("""
                SELECT CallType, count(*) as count 
                FROM fire_df_view 
                WHERE CallType is not null 
                group by CallType 
                order by count desc
                limit 10""")
sql_3.limit(10).display(10)                

# COMMAND ----------

q3_df = fire_df.where("CallType is not null")\
               .select("CallType")\
               .groupBy("CallType")\
               .count()\
               .orderBy("count",ascending=False)\
               .limit(10).display()                

# COMMAND ----------

sql_4 = spark.sql("""
                SELECT CallType, ZipcodeofIncident, count(*) as count 
                FROM fire_df_view 
                WHERE CallType is not null 
                group by CallType, ZipcodeofIncident 
                order by count desc""").limit(10).display()

# COMMAND ----------

q4_df = fire_df.select("CallType","ZipcodeofIncident")\
                .where("CallType is not null")\
                    .groupBy("CallType","ZipcodeofIncident")\
                        .count()\
                            .orderBy("count",ascending=False)\
                                .limit(10).display()

# COMMAND ----------

sql_5 = spark.sql("""
                  SELECT Neighborhood 
                  FROM fire_df_view 
                  WHERE City = 'SF' and 
                  ZipcodeofIncident IN (94102,94103) 
                  LIMIT 10""").display()

# COMMAND ----------

q5_df = fire_df.select("Neighborhood")\
                .where("City == 'SF' and ZipcodeofIncident in (94102,94103)")\
                    .limit(10).display()

# COMMAND ----------

sql_6 = spark.sql("""
                  SELECT sum(NumAlarms), avg(Delay), min(Delay), max(Delay) from fire_df_view""").display()

# COMMAND ----------

q6_df = fire_df.select(expr("sum(NumAlarms) as total_alarms"),avg("Delay").alias('delay_avg'),min("Delay"),max("Delay")).display()

# COMMAND ----------

sql_7 = spark.sql("""
                  SELECT count(DISTINCT year(to_date(CallDate,"MM/DD/YYYY"))) as distinct_year_cnt FROM fire_df_view""").display()

# COMMAND ----------

q7_df = fire_df.select(year(to_date("CallDate","MM/dd/yyyy")).alias("distinct_year"))\
                        .distinct()\
                        .count()
print(q7_df)                        

# COMMAND ----------

q8_df = fire_df.select(weekofyear(to_date("CallDate","MM/dd/yyyy")).alias("week_no"))\
                .where(year(to_date("CallDate","MM/dd/yyyy")) == 2018)\
                    .groupBy("week_no")\
                        .count()\
                            .orderBy("count",ascending=False)
q8_df.display()                                                        

# COMMAND ----------


