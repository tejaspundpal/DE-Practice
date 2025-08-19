-- Databricks notebook source
-- MAGIC %md
-- MAGIC ###Spark using SQL

-- COMMAND ----------

drop table if exists demo_db.fire_service_calls_table;
drop view if exists demo_db;

-- COMMAND ----------

-- MAGIC %fs rm -r dbfs:/user/hive/warehouse/demo_db.db

-- COMMAND ----------

create database if not exists demo_db

-- COMMAND ----------

create table if not exists demo_db.Student(Name varchar(20),ID int) using parquet

-- COMMAND ----------

INSERT INTO demo_db.Student VALUES ('Tejas', 1);

-- COMMAND ----------

SELECT * FROM demo_db.Student

-- COMMAND ----------

CREATE TABLE demo_db.fire_service_calls_table

-- COMMAND ----------

-- MAGIC %python
-- MAGIC spark.conf.set("spark.databricks.delta.schema.autoMerge.enabled", "true")

-- COMMAND ----------

SELECT * FROM global_temp.fire_service_calls_view limit 10;

-- COMMAND ----------

INSERT INTO demo_db.fire_service_calls_table SELECT * FROM global_temp.fire_service_calls_view

-- COMMAND ----------

SELECT count(*) FROM global_temp.fire_service_calls_view

-- COMMAND ----------

SELECT * FROM demo_db.fire_service_calls_tbl LIMIT 10;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #####1.How many distinct types of calls were made to the Fire Department?

-- COMMAND ----------

SELECT count(DISTINCT CallType) as Distinct_Call_Types_Count FROM demo_db.fire_service_calls_tbl WHERE CallType is not null;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #####2.Find out all response for delayed times greater than 5 mins

-- COMMAND ----------

SELECT * FROM demo_db.fire_service_calls_tbl WHERE Delay > 5 LIMIT 10;

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC #####3.What were the most common call types?

-- COMMAND ----------

SELECT max(CallType) FROM demo_db.fire_service_calls_tbl;

-- COMMAND ----------

SELECT CallType, count(*) as count 
FROM demo_db.fire_service_calls_tbl 
WHERE CallType is not null 
group by CallType 
order by count desc
limit 1

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #####4.What zip codes accounted for most common calls?

-- COMMAND ----------

SELECT CallType, Zipcode_of_Incident, count(*) as count 
FROM demo_db.fire_service_calls_tbl 
WHERE CallType is not null 
group by CallType, Zipcode_of_Incident 
order by count desc
limit 1

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #####5.What San Francisco neighborhoods are in the zip codes 94102 and 94103?

-- COMMAND ----------

SELECT Neighborhood FROM demo_db.fire_service_calls_tbl WHERE City = 'SF' and Zipcode_of_Incident IN (94102,94103) LIMIT 10;

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC #####6.What was the sum of all call alarms, average, min and max of the call response time?

-- COMMAND ----------

SELECT sum(NumAlarms), avg(Delay), min(Delay), max(Delay) from demo_db.fire_service_calls_tbl;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #####7.How many distinct years of data in data field?

-- COMMAND ----------

SELECT count(DISTINCT year(to_date(Call_Date,"MM/DD/YYYY"))) as distinct_year_cnt FROM demo_db.fire_service_calls_tbl

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #####8.What week of year 2018 had the most fire calls?

-- COMMAND ----------

select weekofyear(to_date(Call_Date,"MM/DD/YYYY")) as week_no, count(*) as count
from demo_db.fire_service_calls_tbl
where year(to_date(Call_Date,"MM/DD/YYYY")) = 2018
group by week_no
order by count
limit 1

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #####9.What neighborhood in SanFrancisco had the worst response time in 2018?

-- COMMAND ----------

SELECT Neighborhood, Delay FROM demo_db.fire_service_calls_tbl WHERE year(to_date(Call_Date,"MM/DD/YYYY")) = 2018 order by Delay DESC limit 1

-- COMMAND ----------


