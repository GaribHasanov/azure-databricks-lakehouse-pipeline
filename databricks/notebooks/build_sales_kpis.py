from pyspark.sql import SparkSession
from src.utils.config import load_config
from src.etl.gold.sales_kpis import build_sales_kpis

spark = SparkSession.builder.getOrCreate()
config = load_config()

df = spark.read.format("delta").load(
    config.storage.silver_path + "fact_sales/"
)

kpi_df = build_sales_kpis(df)

kpi_df.write.format("delta") \
    .mode("overwrite") \
    .save(config.storage.gold_path + "sales_kpis/")
