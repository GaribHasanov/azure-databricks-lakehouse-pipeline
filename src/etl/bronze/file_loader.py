from src.etl.bronze.ingestion_base import IngestionBase


class FileLoader(IngestionBase):

    def load(self, input_path, output_path):
        df = self.read_json(input_path)
        self.write_delta(df, output_path)
        return df
