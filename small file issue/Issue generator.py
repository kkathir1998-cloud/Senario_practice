from pyspark.sql import functions as F

df = (
    spark.range(0, 50000000)
    .withColumn("customer_id", (F.rand() * 1000000).cast("int"))
    .withColumn("amount", (F.rand() * 10000).cast("double"))
    .orderBy(F.rand())
)

df.repartition(5000) \
  .write \
  .format("delta") \
  .mode("overwrite") \
  .saveAsTable("practice.slow_query_transactions_bad_layout")
