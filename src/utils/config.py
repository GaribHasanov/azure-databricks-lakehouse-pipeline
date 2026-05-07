import os
from dataclasses import dataclass


@dataclass
class Config:
    raw_path: str
    bronze_path: str
    silver_path: str
    gold_path: str


def get_config() -> Config:
    return Config(
        raw_path=os.getenv("RAW_PATH", "/data/raw/"),
        bronze_path=os.getenv("BRONZE_PATH", "/data/bronze/"),
        silver_path=os.getenv("SILVER_PATH", "/data/silver/"),
        gold_path=os.getenv("GOLD_PATH", "/data/gold/")
    )
