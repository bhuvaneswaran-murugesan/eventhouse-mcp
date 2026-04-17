from mcp.client import MCPClient
from llm.orchestrator import Orchestrator

def main():
    print("🚀 Eventhouse NLP Client")

    mcp = MCPClient()
    orchestrator = Orchestrator(mcp)

    while True:
        q = input("🧠 You: ")

        if q.lower() in ["exit", "quit"]:
            break

        answer = orchestrator.ask(q)
        print(f"\n🤖 {answer}\n")

if __name__ == "__main__":
    main()