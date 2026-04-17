from mcp.tools import get_schema, execute_query
from llm.gemini_llm import GeminiClient

class Orchestrator:
    def __init__(self, mcp_client):
        self.mcp = mcp_client
        self.llm = GeminiClient()
        self.history = []

    def ask(self, question):
        schema = get_schema(self.mcp, question)

        prompt = f"""
Schema:
{schema}

Question:
{question}

Return only KQL query.
"""

        kql = self.llm.generate(prompt)

        result = execute_query(self.mcp, kql)

        final_prompt = f"""
Question: {question}
Query: {kql}
Result: {result}

Explain in simple terms.
"""

        answer = self.llm.generate(final_prompt)

        return answer