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
**Logged by:** Tia Sukhnanni  
📅 Sprint Days 1–2 | 💻 JKLU BTech | 🧠 AI + Web + Dev  
