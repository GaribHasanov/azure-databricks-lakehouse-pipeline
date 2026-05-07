from pyspark.sql.types import StructType


def validate_schema(df, expected_schema: StructType):
    return df.schema == expected_schema
