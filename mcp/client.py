import requests
from config.settings import MCP_URL
from auth.authenticate import AzureAuth

class MCPClient:
    def __init__(self):
        self.auth = AzureAuth()
        self.mcp_url = MCP_URL

    def _post(self, method, params=None):
        token = self.auth.get_token()

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        payload = {
            "jsonrpc": "2.0",
            "id": "1",
            "method": method,
            "params": params or {}
        }

        response = requests.post(self.mcp_url, headers=headers, json=payload)

        if response.status_code != 200:
            raise Exception(f"❌ MCP Error: {response.text}")

        return response.json()