# 🤖 LangChain Agentic AI – Sprint Logs

Welcome to my LangChain + LLM exploration as part of a 15-day AI & Dev sprint.  
Here I build, debug, and tune AI agents using LangChain and HuggingFace models — **no paid APIs needed**.

---

## ✅ Agents Built

---

### 🧠 Day 1 – Basic LLM Prompting

📁 File: `hello_llm.py`  
🔹 Goal: Basic text generation using `distilgpt2`

| Feature | Details |
|--------|---------|
| 🛠️ Model Used | `distilgpt2` |
| 📦 Tools | HuggingFace Transformers, LangChain |
| ⚠️ Limitations | No factual QA, mostly text continuation |
| ❌ Problem | GPT-2 returned random, hallucinated stories |

---

### 🧠 Day 2 – Q&A Chatbot (Flan-T5)

📁 File: `hello_llm_chat.py`  
🔹 Goal: Create a terminal chatbot that answers questions meaningfully

| Feature | Details |
|--------|---------|
| 🧠 Model Used | `google/flan-t5-base` |
| 📦 Tools | LangChain, HuggingFace Transformers |
| ✅ Prompting | Instruction-tuned: `"Answer the following question clearly and helpfully"` |
| ✅ Output | Clean, logical, consistent Q&A |
| 🔁 Fixes | Replaced `.run()` with `.invoke()` and tuned tokens |
| 💬 Example: |
You: What is gravity?
🤖 AI: Gravity is a natural force that attracts objects toward one another.

---

## 📌 Learnings So Far

- Prompt tuning dramatically changes LLM output
- GPT-2 isn’t ideal for factual QA — better for storytelling
- Flan-T5 is instruction-following and gives cleaner Q&A
- LangChain `invoke()` is more future-compatible than `run()`

---

# 🤖 Day 3 – AI Agent: Tone-Controlled Chatbot

### ✅ Tech:
- LangChain + HuggingFacePipeline (GPT-2)
- PromptTemplate for sarcasm-based tone

### ✅ What it does:
- Takes user question
- Responds in sarcastic/rude tone using prompt control

### 🚨 Observations:
- GPT2 repeated prompt → replaced with DialoGPT
- Learned limitations of small LLMs
- Prompt formatting (INST-style) improves results

🧠 Day 4 – Study Plan Generator with Flan-T5
📁 File: ai_study_planner.py
🔹 Goal: Use a local HuggingFace model (flan-t5-base) to generate a 15-day study plan for any learning goal without using paid APIs.
| Feature          | Details                                                                                                     |
| ---------------- | ----------------------------------------------------------------------------------------------------------- |
| 🧠 Model Used    | `google/flan-t5-base`                                                                                       |
| 🔗 Tools         | `transformers`, `LangChain`, `HuggingFacePipeline`                                                          |
| 🎯 Prompt        | "You are a strict mentor AI. Write a numbered 15-day study plan..."                                         |
| ✅ Outcome        | User can enter any learning goal (e.g., "learn React in 15 days") and get a clear, actionable day-wise plan |
| 💡 Prompt Format | Multi-line instructions with bullet formatting + rules                                                      |
| 🧪 Fixes         | Replaced broken `.run()` with `.invoke()`, ensured correct output formatting                                |
| 🚫 No APIs       | No OpenAI key needed — everything runs locally using HuggingFace                                            |

📌 Learnings on Day 4
🧠 HuggingFace models like Flan-T5 are great for instruction-following

⚠️ Prompt formatting matters — multi-line prompts with strict instructions improved reliability

🔁 .invoke() is now the standard in LangChain — smoother execution

💻 This task taught how to design prompt-controlled utility agents for real-world productivity tools (like planners)

# 🤖 Agentic AI Assistant – Day 6 Project

An advanced **LangChain-style Agentic AI Assistant** built using Python and Streamlit. It can think, reason, use tools, and respond intelligently to user queries via a chat interface.

---

### ✅ Features

- 📐 Calculator Tool  
- 🧠 Wikipedia Summary Tool  
- 🌐 WebSearch (stub for now)  
- 📄 PDF Summarization Tool  
- 💬 Chat-based Interface with Memory  
- 🌗 Light/Dark Mode Toggle  
- 💾 Save/Load Memory  
- 📥 Download chat as Markdown / JSON  
- 🧩 Upload and process files (PDF/Text)

---

### 🧪 Stack

- `Streamlit` for UI  
- `OpenAI` SDK (supports local base URLs)  
- `LangChain-like tool loop` logic  
-  `Wikipedia`, `dotenv`

---


# 🤖 Agentic AI Assistant – Day 8 Upgrade

## ✅ New Feature
- Improved **UI experience**
  - `Clear Chat` button added with clean rerun behavior
  - Upload PDF/Text with improved file saving logic
  - Better chat bubble formatting and user-agent distinction

## 🛠️ Stack
- Streamlit
- LangChain
- Python (3.10+)
- JSON, PDF Handling
- Dynamic File Tools (tools.py)

## 🔐 Note
API key used locally via `os.environ`.  
This project does **not** expose any secret key in code.  
👉 Make sure to set up `.env` or system-level key for `OPENAI_API_KEY`.

## 📂 Folder Contents
- `ui_app.py`: Main UI logic
- `agent.py`: Tool/chain setup
- `tools.py`: PDF/Text tool integration
- `requirements.txt`: Module list
- `uploads/`: Saved file inputs
- `saved_chat.json`: Loadable memory

---
### 🚀 How to Run these

```bash
pip install -r requirements.txt
streamlit run ui_app.py
```

# 🧠 Day 10-11 – 
# 💬 TiaPrompt — Full-Stack AI Assistant App 
TiaPrompt is a secure, full-stack AI chatbot built with the **MERN stack** (MongoDB, Express.js, React, Node.js). It supports user authentication using session cookies, has a clean React frontend styled with Tailwind CSS, and connects to Mistral AI via API.
--- 
## 🔗 Project Repository 👉 [GitHub – TiaPrompt](https://github.com/TIA1106/TiaPrompt) 
--- 
# 🤖 Tia's Agentic AI Assistant

A personalized AI chatbot built with **Streamlit**, designed to guide Tia in mastering **DSA**, **Full Stack Development**, and **Data Science**. The assistant adapts based on selected learning mode and gives actionable, focused replies. It also supports chat history persistence.
---
## 🔗 Project Repository 👉 [GitHub – tia-agentic-ai](https://github.com/TIA1106/tia-agentic-ai-assistant) 
---

**Logged by:** Tia Sukhnanni  
📅 Sprint Days 1–2 | 💻 JKLU BTech | 🧠 AI + Web + Dev  
