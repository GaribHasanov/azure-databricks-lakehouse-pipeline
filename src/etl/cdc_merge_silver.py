from pyspark.sql import SparkSession
from pyspark.sql.functions import col

from src.utils.config import load_config


def create_spark_session(app_name="LakehousePipeline"):
    return SparkSession.builder.appName(app_name).getOrCreate()


def read_source(spark, path):
    return spark.read.format("json").load(path)


def read_silver(spark, path):
    return spark.read.format("delta").load(path)


def upsert_to_silver(source_df, silver_path, key_col="id"):
    """
    Performs CDC using Delta MERGE INTO:
    - Inserts new records
    - Updates existing records
    """

    source_df.createOrReplaceTempView("source_data")

    merge_query = f"""
    MERGE INTO delta.`{silver_path}` AS target
    USING source_data AS source
    ON target.{key_col} = source.{key_col}

    WHEN MATCHED THEN UPDATE SET *
    WHEN NOT MATCHED THEN INSERT *
    """

    spark.sql(merge_query)


def main():
    config = load_config()
    spark = create_spark_session()

    raw_path = config.storage.raw_path
    silver_path = config.storage.silver_path

    # Read incoming data
    source_df = read_source(spark, raw_path)

    # Ensure silver table exists (in real project: table creation handled separately)
    try:
        read_silver(spark, silver_path)
    except:
        source_df.write.format("delta").mode("overwrite").save(silver_path)

    # Apply CDC merge
    upsert_to_silver(source_df, silver_path)

    print(f"[{config.env}] CDC merge into Silver completed.")


if __name__ == "__main__":
    main()
