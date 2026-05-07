from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, lower, current_timestamp
from pyspark.sql.types import StringType, IntegerType

from src.utils.config import load_config


def create_spark_session(app_name: str = "LakehousePipeline"):
    return SparkSession.builder.appName(app_name).getOrCreate()


def read_bronze(spark, path: str):
    """
    Read Bronze Delta table
    """
    return spark.read.format("delta").load(path)


def clean_data(df):
    """
    Basic data cleaning rules:
    - Trim string fields
    - Lowercase text fields
    - Remove duplicates
    """

    # Example generic transformations (schema unknown yet)
    for field in df.schema.fields:
        if isinstance(field.dataType, StringType):
            df = df.withColumn(field.name, lower(trim(col(field.name))))

    df = df.dropDuplicates()

    return df


def enrich_data(df):
    """
    Add metadata columns for Silver layer
    """
    return df.withColumn("processed_time", current_timestamp())


def write_silver(df, path: str):
    """
    Write cleaned data to Silver layer
    """
    df.write.format("delta") \
        .mode("overwrite") \
        .save(path)


def main():
    config = load_config()
    spark = create_spark_session()

    bronze_path = config.storage.bronze_path
    silver_path = config.storage.silver_path

    # Read
    bronze_df = read_bronze(spark, bronze_path)

    # Transform
    cleaned_df = clean_data(bronze_df)
    silver_df = enrich_data(cleaned_df)

    # Write
    write_silver(silver_df, silver_path)

    print(f"[{config.env}] Silver transformation completed successfully.")


if __name__ == "__main__":
    main()
