from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-small")

llm = HuggingFacePipeline(pipeline=qa_pipeline)

prompt = "What is a black hole?"
response = llm.invoke(prompt)

print("\n AI Response:\n" + response.strip())
