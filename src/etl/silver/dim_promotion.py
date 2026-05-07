from pyspark.sql.functions import col


def build_dim_promotion(df):
    return df.select(
        "promo_id",
        "product_id",
        "discount_percent",
        "start_date",
        "end_date",
        "promo_type"
    )
