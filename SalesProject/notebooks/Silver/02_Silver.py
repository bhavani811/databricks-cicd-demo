# Databricks notebook source
bronze = spark.table("bronze_sales")

# COMMAND ----------

from pyspark.sql.functions import col

silver = (
    bronze
    .withColumn("price", col("price").cast("double"))
    .withColumn("quantity", col("quantity").cast("int"))
    .withColumn("order_id", col("order_id").cast("int"))
)

# COMMAND ----------

silver = silver.na.drop()

# COMMAND ----------

silver = silver.dropDuplicates()

# COMMAND ----------

silver.write \
.mode("overwrite") \
.format("delta") \
.saveAsTable("silver_sales")