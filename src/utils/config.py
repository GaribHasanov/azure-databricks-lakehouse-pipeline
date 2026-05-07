import os
from dataclasses import dataclass


@dataclass
class StorageConfig:
    raw_path: str
    bronze_path: str
    silver_path: str
    gold_path: str


@dataclass
class Config:
    env: str
    storage: StorageConfig


def load_config() -> Config:
    """
    Loads configuration from environment variables.
    In production this can be replaced with Azure Key Vault or Databricks secrets.
    """

    env = os.getenv("ENV", "dev")

    storage = StorageConfig(
        raw_path=os.getenv("RAW_PATH", "/mnt/data/raw/"),
        bronze_path=os.getenv("BRONZE_PATH", "/mnt/data/bronze/"),
        silver_path=os.getenv("SILVER_PATH", "/mnt/data/silver/"),
        gold_path=os.getenv("GOLD_PATH", "/mnt/data/gold/")
    )

    return Config(env=env, storage=storage)
