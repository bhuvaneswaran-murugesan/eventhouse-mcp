import json

def extract_text(result):
    if not result:
        return "⚠️ No response"

    if "error" in result:
        return f"❌ Error: {result['error'].get('message')}"

    content = result.get("result", {}).get("content", [])

    return "\n".join(
        item.get("text", json.dumps(item))
        for item in content if isinstance(item, dict)
    )


def list_tools(client):
    return client._post("tools/list")


def get_schema(client, question):
    return extract_text(
        client._post("tools/call", {
            "name": "getSchema",
            "arguments": {"referenceText": question}
        })
    )


def execute_query(client, query):
    return extract_text(
        client._post("tools/call", {
            "name": "executeQuery",
            "arguments": {
                "kqlQuery": query,
                "maxRecords": 500
            }
        })
    )