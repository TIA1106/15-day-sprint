# 🤖 Day 6 – Agentic AI Assistant (Streamlit + Tools)

This app is an interactive **Agentic AI assistant** built using `LangChain-style logic`, powered by LLMs with tool use, memory, and a responsive Streamlit UI.

### ✅ Features:

- 📐 Calculator Tool  
- 🧠 Wikipedia Summary Tool  
- 🌐 Web Search Stub (extendable)  
- 📄 PDF Summarizer Tool  
- 🧠 Agent memory + loop with tool usage  
- 🌓 Dark/Light mode toggle  
- 💾 Save/Load conversation memory  
- 📦 Download conversation as Markdown/JSON

### 🧪 Stack:
- Python + OpenAI SDK
- Streamlit
- PyPDF2, Wikipedia API
- LangChain-like tool loop logic

---

To run:

```bash
pip install -r requirements.txt
streamlit run ui_app.py
