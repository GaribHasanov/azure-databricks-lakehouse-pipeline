from pyspark.sql.functions import col, lower, trim


def build_dim_product(df):
    return df.select(
        "product_id",
        lower(trim(col("name"))).alias("product_name"),
        "category",
        "brand",
        "price"
    ).dropDuplicates(["product_id"])
