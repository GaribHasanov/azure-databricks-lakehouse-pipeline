from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp

from src.utils.config import load_config


def create_spark_session(app_name: str = "LakehousePipeline"):
    return SparkSession.builder.appName(app_name).getOrCreate()


def read_raw_data(spark, path: str):
    """
    Reads raw data from storage
    """
    return spark.read.format("json").load(path)


def transform_to_bronze(df):
    """
    Add metadata for bronze layer
    """
    return df.withColumn("ingestion_time", current_timestamp())


def write_bronze(df, path: str):
    """
    Write to Delta Bronze layer
    """
    df.write.format("delta") \
        .mode("overwrite") \
        .save(path)


def main():
    # Load config
    config = load_config()

    # Spark session
    spark = create_spark_session()

    # Use config paths
    raw_path = config.storage.raw_path
    bronze_path = config.storage.bronze_path

    # ETL flow
    raw_df = read_raw_data(spark, raw_path)
    bronze_df = transform_to_bronze(raw_df)
    write_bronze(bronze_df, bronze_path)

    print(f"[{config.env}] Bronze ingestion completed successfully.")


if __name__ == "__main__":
    main()
