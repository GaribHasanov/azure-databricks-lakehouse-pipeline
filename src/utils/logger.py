import logging
import json
import os
from datetime import datetime


class JsonFormatter(logging.Formatter):
    """
    Structured logging in JSON format for better observability
    (Azure Log Analytics / Databricks / ELK compatible)
    """

    def format(self, record):
        log_record = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "module": record.name,
            "message": record.getMessage(),
        }

        if hasattr(record, "extra"):
            log_record.update(record.extra)

        return json.dumps(log_record)


def get_logger(name: str = "lakehouse_pipeline"):
    logger = logging.getLogger(name)
    logger.setLevel(os.getenv("LOG_LEVEL", "INFO"))

    handler = logging.StreamHandler()
    handler.setFormatter(JsonFormatter())

    if not logger.handlers:
        logger.addHandler(handler)

    return logger
