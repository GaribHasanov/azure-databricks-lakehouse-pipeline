from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, sum as _sum

from src.utils.config import load_config


def create_spark_session(app_name: str = "LakehousePipeline"):
    return SparkSession.builder.appName(app_name).getOrCreate()


def read_silver(spark, path: str):
    """
    Read Silver Delta table
    """
    return spark.read.format("delta").load(path)


def create_gold_metrics(df):
    """
    Example business aggregations:
    (Generic template — can be adapted per domain)
    """

    # Example aggregation: record count per column value (placeholder logic)
    # In real project this would be domain-specific (sales, users, events, etc.)

    if "category" in df.columns:
        gold_df = df.groupBy("category").agg(
            count("*").alias("total_records")
        )
    else:
        # fallback aggregation
        gold_df = df.select(
            count("*").alias("total_records")
        )

    return gold_df


def write_gold(df, path: str):
    """
    Write Gold layer (analytics-ready data)
    """
    df.write.format("delta") \
        .mode("overwrite") \
        .save(path)


def main():
    config = load_config()
    spark = create_spark_session()

    silver_path = config.storage.silver_path
    gold_path = config.storage.gold_path

    # Read Silver
    silver_df = read_silver(spark, silver_path)

    # Transform to Gold
    gold_df = create_gold_metrics(silver_df)

    # Write Gold
    write_gold(gold_df, gold_path)

    print(f"[{config.env}] Gold layer creation completed successfully.")


if __name__ == "__main__":
    main()
