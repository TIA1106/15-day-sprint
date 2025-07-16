print("🚀 Agent script started")

import os
from openai import OpenAI
from dotenv import load_dotenv
from tools import tools  

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)

print("🔑 API KEY:", os.getenv("OPENAI_API_KEY"))
print("🌍 BASE URL:", os.getenv("OPENAI_BASE_URL"))


def run_agent(user_query, ui=False):
    if ui:
        import streamlit as st

    print("🔁 Agent loop starting...")

    tool_description = """
You are a smart AI assistant. You can think for yourself and answer intelligently.

You also have tools that you can use when needed:

📐 Calculator[expression] — solve math problems  
🧠 Wikipedia[topic] — fetch a short summary of a topic  
🌐 WebSearch[query] — search the web for current info  
📄 SummarizePDF[path] — summarize a given PDF file from path

Use tools **only when needed**. If you're confident, just answer directly.

When you want to use a tool, write:  
Action: ToolName[parameters]

I'll respond with:  
Observation: result
"""

    messages = [
        {"role": "system", "content": f"You are a helpful and smart AI agent. {tool_description}"},
        {"role": "user", "content": user_query}
    ]

    final_response = ""

    while True:
        if ui:
            st.markdown("🧠 **Thinking...**")
        else:
            print("🧠 Sending request to OpenAI...")

        response = client.chat.completions.create(
            model="meta-llama/llama-3-8b-instruct",
            messages=messages,
            temperature=0.7,
            stop=["Observation:"]
        )

        reply = response.choices[0].message.content.strip()
        final_response += f"\n{reply}"
        messages.append({"role": "assistant", "content": reply})

        if ui:
            st.markdown(f"🤖 **Agent:** {reply}")
            if "chat" in st.session_state:
                st.session_state.chat.append({"role": "assistant", "content": reply})
        else:
            print(f"\n🤖 Agent: {reply}")

        if "Action:" in reply:
            action_line = [line for line in reply.split("\n") if "Action:" in line]
            if action_line:
                try:
                    tool_call = action_line[0].split("Action:")[1].strip()
                    tool_name, query = tool_call.split("[")
                    query = query.rstrip("]")

                    tool_name = tool_name.strip()
                    query = query.strip()

                    if ui:
                        st.markdown(f"`Tool:` {tool_name}('{query}')")
                    else:
                        print(f"⚙Tool: {tool_name}('{query}')")

                    result = tools[tool_name](query)

                    if ui:
                        st.markdown(f"`Observation:` {result}")
                    else:
                        print(f"Observation: {result}")

                    messages.append({"role": "user", "content": f"Observation: {result}"})
                except Exception as e:
                    err = f"[Tool Error] {e}"
                    if ui:
                        st.error(err)
                    else:
                        print(err)
                    break
        else:
            break

    return final_response.strip() if ui else None


if __name__ == "__main__":
    print("Waiting for user input")
    user_input = input("Ask your agent: ")
    run_agent(user_input)
