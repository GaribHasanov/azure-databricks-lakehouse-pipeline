import os
from dataclasses import dataclass


@dataclass
class StorageConfig:
    raw_path: str
    bronze_path: str
    silver_path: str
    gold_path: str


@dataclass
class AppConfig:
    storage: StorageConfig
    eventhub_connection_string: str


def load_config() -> AppConfig:
    """
    Central application configuration loader
    """

    storage = StorageConfig(
        raw_path=os.getenv("RAW_PATH", "/mnt/data/raw/"),
        bronze_path=os.getenv("BRONZE_PATH", "/mnt/data/bronze/"),
        silver_path=os.getenv("SILVER_PATH", "/mnt/data/silver/"),
        gold_path=os.getenv("GOLD_PATH", "/mnt/data/gold/")
    )

    return AppConfig(
        storage=storage,
        eventhub_connection_string=os.getenv(
            "EVENTHUB_CONNECTION_STRING",
            ""
        )
    )
