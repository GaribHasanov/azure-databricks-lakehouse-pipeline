from pyspark.sql import SparkSession
from pyspark.sql.functions import sum as _sum, count, avg

from src.utils.config import load_config


def create_spark_session():
    return SparkSession.builder \
        .appName("RetailGoldLayer") \
        .getOrCreate()


def build_store_kpis(df):
    """
    Aggregates sales metrics per store
    """

    return df.groupBy("store_id").agg(
        _sum("total_price").alias("total_revenue"),
        count("transaction_id").alias("total_transactions"),
        avg("total_price").alias("avg_basket_value")
    )


def write_gold(df, path):
    df.write.format("delta") \
        .mode("overwrite") \
        .save(path)


def main():
    config = load_config()
    spark = create_spark_session()

    silver_path = config.storage.silver_path + "fact_sales/"
    gold_path = config.storage.gold_path + "sales_kpis/"

    df = spark.read.format("delta").load(silver_path)

    kpis_df = build_store_kpis(df)

    write_gold(kpis_df, gold_path)

    print("GOLD KPI layer created")


if __name__ == "__main__":
    main()
