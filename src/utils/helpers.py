from pyspark.sql import DataFrame


def deduplicate(df: DataFrame, key: str) -> DataFrame:
    return df.dropDuplicates([key])
