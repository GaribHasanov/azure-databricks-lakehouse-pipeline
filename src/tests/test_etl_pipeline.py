import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

from src.validation.data_validator import DataValidator


@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder \
        .master("local[*]") \
        .appName("LakehouseTests") \
        .getOrCreate()


def test_validator_pass(spark):
    data = [("1", "2024-01-01"), ("2", "2024-01-02")]

    schema = StructType([
        StructField("id", StringType(), True),
        StructField("updated_at", StringType(), True)
    ])

    df = spark.createDataFrame(data, schema)

    validator = DataValidator(
        required_columns=["id", "updated_at"],
        not_null_columns=["id"]
    )

    assert validator.run_all_checks(df) is True


def test_missing_column_fails(spark):
    data = [("1",), ("2",)]

    schema = StructType([
        StructField("id", StringType(), True)
    ])

    df = spark.createDataFrame(data, schema)

    validator = DataValidator(
        required_columns=["id", "updated_at"],
        not_null_columns=["id"]
    )

    with pytest.raises(Exception):
        validator.run_all_checks(df)
