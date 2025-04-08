class APIKeyManager:
    """
    A class to manage and provide multiple API keys for accessing different datasets.
    """

    def __init__(self):
        """
        Initialize the APIKeyManager with a predefined dictionary of API keys.
        """
        self._api_keys = {
            "Frost": "2e243d34-57bc-42b4-8095-239991af5353",
            "Opencage": "e9a6e9b1b9be44fab4720c2c96ae9c48"
        }

    def get_api_key(self, key_name: str) -> str:
        """
        Retrieve the API key for a specific identifier.

        :param key_name: The identifier for the API key (e.g., 'Frost').
        :return: The API key as a string.
        :raises KeyError: If the key_name is not found in the dictionary.
        """
        if key_name not in self._api_keys:
            raise KeyError(f"API key for '{key_name}' not found.")
        return self._api_keys[key_name]


# Eksempel på bruk:
api_key_manager = APIKeyManager()

# Hent Frost API-nøkkelen direkte fra klassen
frost_api_key = api_key_manager.get_api_key("Frost")
print(f"Frost API Key: {frost_api_key}")

# Hent Opencage API-nøkkelen direkte fra klassen
opencage_api_key = api_key_manager.get_api_key("Opencage")
print(f"Opencage API Key: {opencage_api_key}")