from azure.identity import InteractiveBrowserCredential

class AzureAuth:
    def __init__(self):
        self.credential = InteractiveBrowserCredential()

    def get_token(self):
        return self.credential.get_token(
            "https://api.fabric.microsoft.com/.default"
        ).token