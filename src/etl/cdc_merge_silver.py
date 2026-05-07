from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from delta.tables import DeltaTable

from src.utils.config import load_config
from src.utils.logger import get_logger


logger = get_logger(__name__)


def create_spark_session():
    return SparkSession.builder \
        .appName("RetailCDC") \
        .getOrCreate()


def merge_silver(spark, source_df, target_path, key_column):
    """
    Performs CDC MERGE INTO operation
    """

    if DeltaTable.isDeltaTable(spark, target_path):
        target_table = DeltaTable.forPath(spark, target_path)

        target_table.alias("t").merge(
            source_df.alias("s"),
            f"t.{key_column} = s.{key_column}"
        ).whenMatchedUpdateAll(
        ).whenNotMatchedInsertAll(
        ).execute()

        logger.info("CDC MERGE completed successfully")

    else:
        source_df.write.format("delta") \
            .mode("overwrite") \
            .save(target_path)

        logger.info("Initial load completed (no existing table)")


def main():
    config = load_config()
    spark = create_spark_session()

    source_path = config.storage.bronze_path + "sales_transactions/"
    target_path = config.storage.silver_path + "fact_sales/"

    source_df = spark.read.format("delta").load(source_path)

    merge_silver(
        spark=spark,
        source_df=source_df,
        target_path=target_path,
        key_column="transaction_id"
    )


if __name__ == "__main__":
    main()
