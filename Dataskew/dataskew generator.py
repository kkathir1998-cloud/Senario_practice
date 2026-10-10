from pyspark.sql import functions as F

fact = (
    spark.range(0, 100_000_000)
    .withColumn(
        "customer_id",
        F.when(F.rand() < 0.99, 1)
         .otherwise((F.rand() * 100000).cast("int"))
    )
    .withColumn("amount", F.round(F.rand() * 1000, 2))
)

fact.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.practice.skewed_fact")

dim = (
    spark.range(1, 100001)
    .withColumnRenamed("id", "customer_id")
    .withColumn("region", F.lit("APAC"))
)

dim.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.practice.customer_dim")
