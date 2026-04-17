import streamlit as st
from mcp.client import MCPClient
from orchestrator.orchestrator import Orchestrator
from llm.factory import get_llm

# -----------------------
# Init session state
# -----------------------
if "chat" not in st.session_state:
    st.session_state.chat = []

if "model" not in st.session_state:
    st.session_state.model = "Gemini"

if "orchestrator" not in st.session_state:
    st.session_state.orchestrator = None   # ❗ lazy init

# -----------------------
# UI
# -----------------------
st.title("🚀 Eventhouse NLP Chat")

selected_model = st.selectbox(
    "🤖 Select Model",
    ["Gemini", "Azure OpenAI"]
)

st.session_state.model = selected_model

# -----------------------
# Chat UI
# -----------------------
for role, msg in st.session_state.chat:
    with st.chat_message(role):
        st.markdown(msg)

# -----------------------
# Input
# -----------------------
user_input = st.chat_input("Ask your database...")

if user_input:
    st.session_state.chat.append(("user", user_input))

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            try:
                # ✅ Initialize only when needed
                if st.session_state.orchestrator is None:
                    mcp = MCPClient()
                    llm = get_llm(st.session_state.model)
                    st.session_state.orchestrator = Orchestrator(mcp, llm)

                else:
                    # update model dynamically
                    llm = get_llm(st.session_state.model)
                    st.session_state.orchestrator.set_llm(llm)

                response = st.session_state.orchestrator.ask(user_input)

            except Exception as e:
                response = f"❌ Error: {str(e)}"

        st.markdown(response)

    st.session_state.chat.append(("assistant", response))