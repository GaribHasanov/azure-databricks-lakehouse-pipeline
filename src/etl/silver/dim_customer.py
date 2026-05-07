from pyspark.sql.functions import col


def build_dim_customer(df):
    return df.select(
        "customer_id",
        "first_name",
        "last_name",
        "age_group",
        "gender",
        "city",
        "loyalty_status"
    ).dropDuplicates(["customer_id"])
