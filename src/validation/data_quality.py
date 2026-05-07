from pyspark.sql.functions import col


class DataQualityValidator:

    def __init__(self, df):
        self.df = df
        self.errors = []

    def check_nulls(self, columns):
        for c in columns:
            if self.df.filter(col(c).isNull()).count() > 0:
                self.errors.append(f"NULL values in {c}")
        return self

    def check_duplicates(self, key):
        if self.df.groupBy(key).count().filter("count > 1").count() > 0:
            self.errors.append(f"DUPLICATES in {key}")
        return self

    def check_positive(self, column):
        if self.df.filter(col(column) < 0).count() > 0:
            self.errors.append(f"NEGATIVE values in {column}")
        return self

    def is_valid(self):
        return len(self.errors) == 0

    def report(self):
        return self.errors
