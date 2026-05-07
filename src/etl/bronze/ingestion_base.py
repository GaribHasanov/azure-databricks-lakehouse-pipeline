from pyspark.sql import SparkSession


class IngestionBase:

    def __init__(self):
        self.spark = SparkSession.builder.getOrCreate()

    def read_json(self, path):
        return self.spark.read.json(path)

    def write_delta(self, df, path):
        df.write.format("delta").mode("overwrite").save(path)
