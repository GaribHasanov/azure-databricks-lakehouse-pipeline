from pyspark.sql import SparkSession
from src.utils.config import load_config
from src.etl.silver.fact_sales import build_fact_sales

spark = SparkSession.builder.getOrCreate()
config = load_config()

df = spark.read.format("delta").load(
    config.storage.bronze_path + "sales_transactions/"
)

fact_df = build_fact_sales(df)

fact_df.write.format("delta") \
    .mode("overwrite") \
    .save(config.storage.silver_path + "fact_sales/")
