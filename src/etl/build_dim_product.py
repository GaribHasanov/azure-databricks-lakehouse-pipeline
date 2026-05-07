from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, trim

from src.utils.config import load_config


def transform_dim_product(df):
    """
    Cleans and structures product dimension table
    """

    return df.select(
        col("product_id"),
        lower(trim(col("name"))).alias("product_name"),
        col("category"),
        col("brand"),
        col("price")
    ).dropDuplicates(["product_id"])


def main():
    config = load_config()
    spark = SparkSession.builder.appName("RetailLakehouse").getOrCreate()

    bronze_path = config.storage.bronze_path + "products/"
    silver_path = config.storage.silver_path + "dim_product/"

    df = spark.read.format("delta").load(bronze_path)

    dim_df = transform_dim_product(df)

    dim_df.write.format("delta").mode("overwrite").save(silver_path)

    print("DIM PRODUCT created successfully")


if __name__ == "__main__":
    main()
