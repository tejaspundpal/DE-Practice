from pyspark.sql import *

spark = SparkSession.builder.appName("pyspark1").getOrCreate()

datalist = [("Tejas", 1), ("Shubham", 2), ("Om", 3), ("Kedar", 4)]
df = spark.createDataFrame(datalist, ["Name", "Id"])
df.show()