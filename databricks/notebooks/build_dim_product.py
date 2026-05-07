from pyspark.sql import SparkSession
from src.utils.config import load_config
from src.etl.silver.dim_product import build_dim_product

spark = SparkSession.builder.getOrCreate()
config = load_config()

df = spark.read.format("delta").load(
    config.storage.bronze_path + "products/"
)

dim_df = build_dim_product(df)

dim_df.write.format("delta") \
    .mode("overwrite") \
    .save(config.storage.silver_path + "dim_product/")
