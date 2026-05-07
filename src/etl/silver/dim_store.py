from pyspark.sql.functions import col, lower, trim


def build_dim_store(df):
    return df.select(
        "store_id",
        lower(trim(col("city"))).alias("city"),
        lower(trim(col("region"))).alias("region"),
        "store_size",
        "opening_date"
    ).dropDuplicates(["store_id"])
