import os


class SecretsManager:
    """
    Handles secure secret retrieval
    """

    @staticmethod
    def get_secret(secret_name: str) -> str:
        """
        Returns secret from environment variables
        """

        value = os.getenv(secret_name)

        if not value:
            raise ValueError(
                f"Missing required secret: {secret_name}"
            )

        return value
