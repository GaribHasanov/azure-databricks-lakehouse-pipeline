from pyspark.sql.functions import sum, count, avg


def build_sales_kpis(df):

    return df.groupBy("store_id").agg(
        sum("total_price").alias("total_revenue"),
        count("transaction_id").alias("total_transactions"),
        avg("total_price").alias("avg_basket_value")
    )
