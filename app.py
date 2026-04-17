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
    mcp = MCPClient()
    llm = get_llm("Gemini")
    st.session_state.orchestrator = Orchestrator(mcp, llm)

# -----------------------
# UI Title
# -----------------------
st.title("🚀 Eventhouse NLP Chat")

# -----------------------
# Model Switch (Dropdown)
# -----------------------
selected_model = st.selectbox(
    "🤖 Select Model",
    ["Gemini", "OpenAI"],
    index=0 if st.session_state.model == "Gemini" else 1
)

# Update model dynamically
if selected_model != st.session_state.model:
    st.session_state.model = selected_model
    new_llm = get_llm(selected_model)
    st.session_state.orchestrator.set_llm(new_llm)
    st.success(f"Switched to {selected_model}")

# -----------------------
# Chat Display
# -----------------------
for role, msg in st.session_state.chat:
    with st.chat_message(role):
        st.markdown(msg)

# -----------------------
# User Input
# -----------------------
user_input = st.chat_input("Ask your database...")

if user_input:
    st.session_state.chat.append(("user", user_input))

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.orchestrator.ask(user_input)
            st.markdown(response)

    st.session_state.chat.append(("assistant", response))