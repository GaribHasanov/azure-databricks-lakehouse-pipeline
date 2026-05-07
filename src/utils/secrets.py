import os


class SecretsManager:

    @staticmethod
    def get(secret_name: str) -> str:
        value = os.getenv(secret_name)

        if not value:
            raise Exception(f"Missing secret: {secret_name}")

        return value
