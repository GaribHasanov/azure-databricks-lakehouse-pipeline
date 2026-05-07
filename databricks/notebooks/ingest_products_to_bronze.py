from pyspark.sql import SparkSession
from src.utils.config import load_config
from src.etl.bronze.file_loader import FileLoader

spark = SparkSession.builder.getOrCreate()
config = load_config()

loader = FileLoader()

df = loader.load(
    config.storage.raw_path + "products/",
    config.storage.bronze_path + "products/"
)
