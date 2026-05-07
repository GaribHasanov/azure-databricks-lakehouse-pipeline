from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, trim

from src.utils.config import load_config


def create_spark_session():
    return SparkSession.builder \
        .appName("RetailDimProduct") \
        .getOrCreate()


def transform_dim_product(df):
    """
    Clean product master data for dimension table
    """

    return df.select(
        col("product_id"),
        lower(trim(col("name"))).alias("product_name"),
        col("category"),
        col("brand"),
        col("price")
    ).dropDuplicates(["product_id"])


def write_dim(df, path):
    df.write.format("delta") \
        .mode("overwrite") \
        .save(path)


def main():
    config = load_config()
    spark = create_spark_session()

    bronze_path = config.storage.bronze_path + "products/"
    silver_path = config.storage.silver_path + "dim_product/"

    df = spark.read.format("delta").load(bronze_path)

    dim_df = transform_dim_product(df)

    write_dim(dim_df, silver_path)

    print("DIM PRODUCT created")


if __name__ == "__main__":
    main()
