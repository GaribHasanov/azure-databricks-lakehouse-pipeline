from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, trim

from src.utils.config import load_config


def create_spark_session():
    return SparkSession.builder \
        .appName("RetailDimStore") \
        .getOrCreate()


def transform_dim_store(df):
    """
    Cleans store master data
    """

    return df.select(
        col("store_id"),
        lower(trim(col("city"))).alias("city"),
        lower(trim(col("region"))).alias("region"),
        col("store_size"),
        col("opening_date")
    ).dropDuplicates(["store_id"])


def write_dim(df, path):
    df.write.format("delta") \
        .mode("overwrite") \
        .save(path)


def main():
    config = load_config()
    spark = create_spark_session()

    bronze_path = config.storage.bronze_path + "stores/"
    silver_path = config.storage.silver_path + "dim_store/"

    df = spark.read.format("delta").load(bronze_path)

    dim_df = transform_dim_store(df)

    write_dim(dim_df, silver_path)

    print("DIM STORE created")


if __name__ == "__main__":
    main()
