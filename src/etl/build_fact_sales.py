from pyspark.sql import SparkSession
from pyspark.sql.functions import col

from src.utils.config import load_config


def create_fact_sales(df):
    """
    Converts raw sales into fact table
    """

    return df.select(
        col("transaction_id"),
        col("product_id"),
        col("store_id"),
        col("customer_id"),
        col("quantity"),
        col("unit_price"),
        (col("quantity") * col("unit_price")).alias("total_price"),
        col("timestamp")
    )


def main():
    config = load_config()
    spark = SparkSession.builder.appName("RetailLakehouse").getOrCreate()

    bronze_path = config.storage.bronze_path + "sales_transactions/"
    gold_path = config.storage.gold_path + "fact_sales/"

    df = spark.read.format("delta").load(bronze_path)

    fact_df = create_fact_sales(df)

    fact_df.write.format("delta").mode("overwrite").save(gold_path)

    print("FACT SALES created successfully")


if __name__ == "__main__":
    main()
