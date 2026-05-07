from pyspark.sql.functions import col


def validate_sales_rules(df):
    return df.filter(
        (col("quantity") > 0) &
        (col("unit_price") > 0)
    )
