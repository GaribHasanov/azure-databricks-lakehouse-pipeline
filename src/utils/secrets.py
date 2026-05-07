import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient


class SecretManager:
    def __init__(self, key_vault_url: str):
        """
        Initializes Azure Key Vault client
        """
        credential = DefaultAzureCredential()
        self.client = SecretClient(vault_url=key_vault_url, credential=credential)

    def get_secret(self, secret_name: str) -> str:
        """
        Fetch a secret from Azure Key Vault
        """
        return self.client.get_secret(secret_name).value


def get_databricks_token():
    """
    Fallback: environment variable or Key Vault
    """
    kv_url = os.getenv("KEY_VAULT_URL")

    if kv_url:
        manager = SecretManager(kv_url)
        return manager.get_secret("DATABRICKS-TOKEN")

    return os.getenv("DATABRICKS_TOKEN")
