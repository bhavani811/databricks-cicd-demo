# Databricks notebook source
df = spark.table("silver_sales")

# COMMAND ----------

from pyspark.sql.functions import col

df = df.withColumn(
    "sales",
    col("price") * col("quantity")
)

# COMMAND ----------

from pyspark.sql.functions import col

df = df.withColumn(
    "sales",
    col("price") * col("quantity")
)

# COMMAND ----------

from pyspark.sql.functions import sum

gold = (
    df.groupBy("customer")
      .agg(sum("sales").alias("total_sales"))
)

# COMMAND ----------

gold.write.mode("overwrite") \
.format("delta") \
.saveAsTable("gold_sales")