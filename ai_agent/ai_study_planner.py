from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
llm_pipeline = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=300,
    temperature=0.7,
    top_k=50,
    top_p=0.95
)
llm = HuggingFacePipeline(pipeline=llm_pipeline)

template = """
You are a strict AI mentor. Write a 15-day day-wise study plan to achieve this goal: {goal}

Rules:
- Numbered bullet points (1 to 15)
- Only 1 actionable task per day
- No extra explanation or intro
"""

prompt = PromptTemplate(input_variables=["goal"], template=template)
chain = LLMChain(llm=llm, prompt=prompt)

print("🎯 Mentor AI – Enter your learning goal (type 'exit' to stop):")
while True:
    goal = input("You: ")
    if goal.lower().strip() == "exit":
        print("✅ Session ended.")
        break

    result = chain.invoke({"goal": goal})
    print("\n📅 Study Plan:\n" + result["text"].strip())
