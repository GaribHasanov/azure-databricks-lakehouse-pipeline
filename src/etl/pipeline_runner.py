from src.etl.silver.fact_sales import build_fact_sales


class PipelineRunner:

    def run_fact_sales(self, df):
        return build_fact_sales(df)
