from .core.config import settings
import requests #type: ignore
from flowx_sdk.cli import FlowxCLI

class Client:
    def __init__(self, api_key: str) -> None:
        self.flowx_cli = FlowxCLI()
        self.api_key = api_key
        self._base_url = settings.base_url
        self.authenticated = False #type: ignore

        # Initialize the http client (requests)
        self.session = requests.Session()

        # Attempt to authenticate on initialization
        self.authenticate()
    

    def authenticate(self):
        """Authenticate with the API using the provided API key."""
        self.flowx_cli.load_flowx_env()
        
        auth_url = f"{self._base_url}/verify-token/{self.api_key}"
        print(f"Authenticating with URL: {auth_url}")  # Debugging

        payload = {}
        headers = {'Authorization': f"Bearer {self.flowx_cli.get_access_token()}"} # Use X-Token header for authentication
        print(f"Headers: {headers}")  # Debugging


        # end a GET or POST request to verify the API key
        response = self.session.get(auth_url, headers=headers, data=payload)
        print(response.status_code)
        print(response)

        if response.status_code == 200:
            self.authenticated = True
            print("Authenticated successfully")
        else:
            self.authenticated = False
            print("Authentication failed 🌋 please check you API-Token ")

    def get_supported_currencies(self) -> dict:
        supported_currencies = {
            "stablecoins": ["USDT", "USDC", "DAI", "BUSD", "EUROC"],
            "african_fiat": ["NGN", "KES", "ZAR", "GHS", "TZS", "UGX"],
            "global_fiat": ["USD", "EUR", "GBP"],
            "cryptocurrencies": ["SUI", "BTC", "ETH", "XRP"]
        }
        return supported_currencies