from mcp.tools import get_schema, execute_query

class Orchestrator:
    def __init__(self, mcp_client, llm):
        self.mcp = mcp_client
        self.llm = llm

    def set_llm(self, llm):
        self.llm = llm

    def ask(self, question):
        schema = get_schema(self.mcp, question)

        kql_prompt = f"""
        Schema:
        {schema}

        Question:
        {question}

        Return only KQL query.
        """

        kql = self.llm.generate(kql_prompt)

        result = execute_query(self.mcp, kql)

        final_prompt = f"""
        Question: {question}
        Query: {kql}
        Result: {result}

        Explain clearly.
        """

        return self.llm.generate(final_prompt)