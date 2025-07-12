from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
llm_pipeline = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=100
)
llm = HuggingFacePipeline(pipeline=llm_pipeline)
prompt = PromptTemplate(
    input_variables=["question"],
    template="Answer the following question clearly and helpfully:\n\n{question}"
)
chain = LLMChain(llm=llm, prompt=prompt)

print("Ask me anything! (type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chain.invoke({"question": user_input})
    print("🤖 AI:", response["text"].strip())
