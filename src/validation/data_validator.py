from pyspark.sql import DataFrame
from pyspark.sql.functions import col


class DataValidator:
    """
    Simple schema + data quality validation layer
    """

    def __init__(self, required_columns: list, not_null_columns: list):
        self.required_columns = required_columns
        self.not_null_columns = not_null_columns

    def validate_schema(self, df: DataFrame):
        missing_cols = [
            c for c in self.required_columns if c not in df.columns
        ]

        if missing_cols:
            raise Exception(f"Missing required columns: {missing_cols}")

        return True

    def validate_not_nulls(self, df: DataFrame):
        for col_name in self.not_null_columns:
            null_count = df.filter(col(col_name).isNull()).count()

            if null_count > 0:
                raise Exception(
                    f"Column '{col_name}' has {null_count} null values"
                )

        return True

    def run_all_checks(self, df: DataFrame):
        self.validate_schema(df)
        self.validate_not_nulls(df)
        return True
