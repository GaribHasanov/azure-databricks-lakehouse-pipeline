from delta.tables import DeltaTable


def merge_delta(spark, df, path, key):

    if DeltaTable.isDeltaTable(spark, path):

        target = DeltaTable.forPath(spark, path)

        target.alias("t").merge(
            df.alias("s"),
            f"t.{key} = s.{key}"
        ).whenMatchedUpdateAll() \
         .whenNotMatchedInsertAll() \
         .execute()

    else:
        df.write.format("delta").mode("overwrite").save(path)
