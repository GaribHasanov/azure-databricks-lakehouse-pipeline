from pyspark.sql.functions import col


def build_fact_sales(df):
    return df.select(
        "transaction_id",
        "timestamp",
        "store_id",
        "customer_id",
        "product_id",
        "quantity",
        "unit_price",
        (col("quantity") * col("unit_price")).alias("total_price")
    )
