# Databricks notebook source


# COMMAND ----------

df = (
    spark.read
         .option("header", "true")
         .csv("/Volumes/workspace/default/cicd_volume/sales.csv")
)

display(df)

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df.write.mode("overwrite") \
    .format("delta") \
    .saveAsTable("bronze_sales")

# COMMAND ----------

display(spark.table("bronze_sales"))