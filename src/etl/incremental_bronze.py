from pyspark.sql import SparkSession
from pyspark.sql.functions import col, max as _max

from src.utils.config import load_config


def create_spark_session(app_name="LakehousePipeline"):
    return SparkSession.builder.appName(app_name).getOrCreate()


def read_source(spark, path):
    return spark.read.format("json").load(path)


def read_existing_bronze(spark, path):
    try:
        return spark.read.format("delta").load(path)
    except:
        return None


def get_max_timestamp(df, timestamp_col):
    if df is None or df.rdd.isEmpty():
        return None
    return df.select(_max(col(timestamp_col))).collect()[0][0]


def filter_incremental(df, last_timestamp, timestamp_col="updated_at"):
    if last_timestamp is None:
        return df

    return df.filter(col(timestamp_col) > last_timestamp)


def write_bronze(df, path):
    df.write.format("delta") \
        .mode("append") \
        .save(path)


def main():
    config = load_config()
    spark = create_spark_session()

    raw_path = config.storage.raw_path
    bronze_path = config.storage.bronze_path

    # Read data
    source_df = read_source(spark, raw_path)
    existing_bronze_df = read_existing_bronze(spark, bronze_path)

    # Determine last processed timestamp
    last_ts = get_max_timestamp(existing_bronze_df, "updated_at")

    # Filter only new records
    incremental_df = filter_incremental(source_df, last_ts)

    # Write only new data
    write_bronze(incremental_df, bronze_path)

    print(f"[{config.env}] Incremental ingestion completed.")


if __name__ == "__main__":
    main()
