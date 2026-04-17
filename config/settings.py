from dotenv import load_dotenv
import os

load_dotenv()

# =========================
# 🔷 FABRIC MCP CONFIG
# =========================
WORKSPACE_ID = os.getenv("WORKSPACE_ID", "")
DATABASE_ID = os.getenv("DATABASE_ID", "")

MCP_URL = f"https://api.fabric.microsoft.com/v1/mcp/workspaces/{WORKSPACE_ID}/kqlDatabases/{DATABASE_ID}"

# =========================
# 🤖 GEMINI CONFIG
# =========================
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.0-flash"

# =========================
# 🤖 AZURE OPENAI CONFIG
# =========================
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY", "")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT", "")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT", "")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "")