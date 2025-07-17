import streamlit as st
import os
import base64
import json
from agent import run_agent

st.set_page_config(page_title="Agentic AI Assistant", layout="centered")

st.sidebar.title("⚙️ Settings")
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

theme_choice = st.sidebar.radio("Theme Mode", ["light", "dark"], index=0 if st.session_state.theme == "light" else 1)
st.session_state.theme = theme_choice
theme = st.session_state.theme

st.markdown(f"""
    <style>
    html, body, .stApp, .block-container {{
        background-color: {"#0e1117" if theme == "dark" else "white"} !important;
        color: {"white" if theme == "dark" else "black"} !important;
    }}
    section[data-testid="stSidebar"] {{
        background-color: {"#1c1c1c" if theme == "dark" else "#f5f5f5"} !important;
        color: {"white" if theme == "dark" else "black"} !important;
    }}
    [data-testid="collapsedControl"] {{
        background-color: {"#333" if theme == "dark" else "#ccc"} !important;
        color: {"white" if theme == "dark" else "black"} !important;
        border-radius: 6px;
        padding: 6px;
        position: fixed;
        top: 10px;
        left: 10px;
        z-index: 9999;
    }}
    .chat-bubble {{
        padding: 1rem;
        border-radius: 1rem;
        margin: 0.5rem 0;
        max-width: 80%;
        word-wrap: break-word;
    }}
    .user {{
        margin-left: auto;
        background-color: {"#1a5dab" if theme == "dark" else "#cce5ff"};
        color: white;
        text-align: right;
    }}
    .agent {{
        margin-right: auto;
        background-color: {"#333" if theme == "dark" else "#f0f0f0"};
        color: {"white" if theme == "dark" else "black"};
    }}
    input, textarea {{
        background-color: {"#222" if theme == "dark" else "#fff"} !important;
        color: {"white" if theme == "dark" else "black"} !important;
        border-radius: 8px;
        padding: 0.5rem;
    }}
    ::placeholder {{
        color: {"#aaa" if theme == "dark" else "#555"} !important;
    }}
    .stButton > button {{
        background-color: {"#1e90ff" if theme == "dark" else "#007bff"} !important;
        color: white !important;
        font-weight: 600;
        padding: 0.4rem 1rem;
        border: none;
        border-radius: 6px;
        margin-top: 0.5rem;
    }}
    .stButton > button:hover {{
        background-color: {"#187bcd" if theme == "dark" else "#0056b3"} !important;
    }}
    </style>
""", unsafe_allow_html=True)

st.title("🧠 Agentic AI Assistant")

if "chat" not in st.session_state:
    st.session_state.chat = []

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("💬 Message", placeholder="Ask anything...")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    st.session_state.chat.append({"role": "user", "content": user_input})
    run_agent(user_input, ui=True)

for msg in st.session_state.chat:
    role = msg["role"]
    content = msg["content"]
    bubble_class = "user" if role == "user" else "agent"
    st.markdown(
        f"<div class='chat-bubble {bubble_class}'><b>{'👤 You' if role == 'user' else '🤖 Agent'}:</b><br>{content}</div>",
        unsafe_allow_html=True
    )

if st.button("🧹 Clear Chat"):
    st.session_state.chat = []
    st.rerun()

uploaded_file = st.file_uploader("📎 Upload a file (PDF/Text)", type=["pdf", "txt"])
if uploaded_file:
    filename = f"uploads/{uploaded_file.name}"
    os.makedirs("uploads", exist_ok=True)
    with open(filename, "wb") as f:
        f.write(uploaded_file.read())

    if st.button("📄 Summarize This File"):
        tool_call = f"SummarizePDF[{filename}]"
        st.session_state.chat.append({"role": "user", "content": tool_call})
        run_agent(tool_call, ui=True)

def download_chat(format="markdown"):
    if format == "markdown":
        content = "\n\n".join([f"**You:** {m['content']}" if m['role'] == "user" else f"**Agent:** {m['content']}" for m in st.session_state.chat])
        mime = "text/markdown"
        ext = "md"
    else:
        content = json.dumps(st.session_state.chat, indent=2)
        mime = "application/json"
        ext = "json"

    b64 = base64.b64encode(content.encode()).decode()
    href = f'<a href="data:{mime};base64,{b64}" download="conversation.{ext}">📥 Download as {ext.upper()}</a>'
    st.markdown(href, unsafe_allow_html=True)

st.markdown("### 📦 Export Options")
download_chat("markdown")
download_chat("json")

with st.expander("💾 Save/Load Memory"):
    if st.button("💾 Save Now"):
        with open("saved_chat.json", "w") as f:
            json.dump(st.session_state.chat, f)
        st.success("✅ Chat saved!")

    if st.button("Load Last Save"):
        try:
            with open("saved_chat.json", "r") as f:
                st.session_state.chat = json.load(f)
            st.success("✅ Chat loaded!")
        except:
            st.warning("No saved chat found.")
