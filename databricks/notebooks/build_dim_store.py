from pyspark.sql import SparkSession
from src.utils.config import load_config
from src.etl.silver.dim_store import build_dim_store

spark = SparkSession.builder.getOrCreate()
config = load_config()

df = spark.read.format("delta").load(
    config.storage.raw_path + "stores/"
)

dim_df = build_dim_store(df)

dim_df.write.format("delta") \
    .mode("overwrite") \
    .save(config.storage.silver_path + "dim_store/")
