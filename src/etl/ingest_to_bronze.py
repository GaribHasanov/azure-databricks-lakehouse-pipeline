from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp


def create_spark_session(app_name: str = "LakehousePipeline"):
    return SparkSession.builder.appName(app_name).getOrCreate()


def read_raw_data(spark, path: str):
    """
    Reads raw data from ADLS / local storage
    """
    return spark.read.format("json").load(path)


def transform_to_bronze(df):
    """
    Minimal transformations for Bronze layer:
    - Add ingestion timestamp
    - Keep raw structure intact
    """
    return df.withColumn("ingestion_time", current_timestamp())


def write_bronze(df, output_path: str):
    """
    Writes data to Bronze layer in Delta format
    """
    df.write.format("delta") \
        .mode("overwrite") \
        .save(output_path)


def main():
    # Initialize Spark
    spark = create_spark_session()

    # Paths (later we can move these to config)
    raw_path = "/mnt/data/raw/"
    bronze_path = "/mnt/data/bronze/"

    # ETL flow
    raw_df = read_raw_data(spark, raw_path)
    bronze_df = transform_to_bronze(raw_df)
    write_bronze(bronze_df, bronze_path)

    print("Bronze layer ingestion completed successfully.")


if __name__ == "__main__":
    main()
