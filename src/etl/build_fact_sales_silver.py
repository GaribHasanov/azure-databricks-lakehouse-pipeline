from pyspark.sql import SparkSession
from pyspark.sql.functions import col

from src.utils.config import load_config


def create_spark_session():
    return SparkSession.builder \
        .appName("RetailSilverLayer") \
        .getOrCreate()


def transform_to_fact_sales(df):
    """
    Builds fact_sales table from Bronze data
    """

    return df.select(
        col("transaction_id"),
        col("timestamp"),
        col("store_id"),
        col("customer_id"),
        col("product_id"),
        col("quantity"),
        col("unit_price"),
        (col("quantity") * col("unit_price")).alias("total_price")
    )


def write_silver(df, path):
    df.write.format("delta") \
        .mode("overwrite") \
        .save(path)


def main():
    config = load_config()
    spark = create_spark_session()

    bronze_path = config.storage.bronze_path + "sales_transactions/"
    silver_path = config.storage.silver_path + "fact_sales/"

    df = spark.read.format("delta").load(bronze_path)

    fact_df = transform_to_fact_sales(df)

    write_silver(fact_df, silver_path)

    print("Silver fact_sales created")


if __name__ == "__main__":
    main()
