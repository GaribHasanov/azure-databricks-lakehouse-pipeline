from pyspark.sql import SparkSession
from src.utils.config import load_config
from src.etl.bronze.file_loader import FileLoader

spark = SparkSession.builder.getOrCreate()
config = load_config()

loader = FileLoader()

input_path = config.storage.raw_path + "sales_transactions/"
output_path = config.storage.bronze_path + "sales_transactions/"

df = loader.load(input_path, output_path)
