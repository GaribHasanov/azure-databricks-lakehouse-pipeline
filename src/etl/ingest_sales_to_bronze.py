from pyspark.sql import SparkSession
from src.utils.config import load_config


def create_spark_session():
    return SparkSession.builder \
        .appName("RetailBronzeIngestion") \
        .getOrCreate()


def read_raw_data(spark, path):
    """
    Reads raw sales JSON data
    """
    return spark.read.format("json").load(path)


def write_bronze(df, path):
    """
    Writes data into Bronze layer (Delta format)
    """
    df.write.format("delta") \
        .mode("overwrite") \
        .save(path)


def main():
    config = load_config()
    spark = create_spark_session()

    raw_path = config.storage.raw_path + "sales_transactions/"
    bronze_path = config.storage.bronze_path + "sales_transactions/"

    df = read_raw_data(spark, raw_path)

    write_bronze(df, bronze_path)

    print("Bronze ingestion completed")


if __name__ == "__main__":
    main()
