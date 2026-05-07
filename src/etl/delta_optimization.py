from pyspark.sql import SparkSession


def optimize_bronze_table(path: str):
    """
    Runs Delta OPTIMIZE and compaction
    """
    spark.sql(f"OPTIMIZE delta.`{path}`")


def zorder_bronze_table(path: str, columns: list):
    """
    Applies ZORDER clustering for faster query performance
    """
    cols = ", ".join(columns)
    spark.sql(f"OPTIMIZE delta.`{path}` ZORDER BY ({cols})")


def vacuum_table(path: str, retention_hours: int = 168):
    """
    Removes old files (default 7 days retention)
    """
    spark.sql(f"VACUUM delta.`{path}` RETAIN {retention_hours} HOURS")


def main():
    spark = SparkSession.builder.appName("DeltaOptimization").getOrCreate()

    bronze_path = "/mnt/data/bronze/"
    silver_path = "/mnt/data/silver/"
    gold_path = "/mnt/data/gold/"

    # -------------------
    # Bronze optimization
    # -------------------
    optimize_bronze_table(bronze_path)
    zorder_bronze_table(bronze_path, ["id", "updated_at"])

    # -------------------
    # Silver optimization
    # -------------------
    optimize_bronze_table(silver_path)
    zorder_bronze_table(silver_path, ["id"])

    # -------------------
    # Gold optimization
    # -------------------
    optimize_bronze_table(gold_path)

    # Cleanup old files
    vacuum_table(bronze_path)
    vacuum_table(silver_path)

    print("Delta optimization completed successfully.")


if __name__ == "__main__":
    main()
