
import math
import wikipedia
import PyPDF2
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)

def Calculator(expr):
    try:
        return eval(expr)
    except:
        return "Invalid math expression"

def Wikipedia(topic):
    try:
        return wikipedia.summary(topic, sentences=2)
    except Exception as e:
        return f"Wikipedia error: {e}"

def WebSearch(query):
    return f"WebSearch is not implemented yet. Query: {query}"

def SummarizePDF(path):
    try:
        reader = PyPDF2.PdfReader(path)
        full_text = ""
        for page in reader.pages:
            full_text += page.extract_text() or ""
        full_text = full_text.strip()

        if len(full_text) < 100:
            return "PDF too short or empty."

        response = client.chat.completions.create(
            model="meta-llama/llama-3-8b-instruct",
            messages=[
                {"role": "system", "content": "You are a summarizer. Summarize clearly and briefly."},
                {"role": "user", "content": full_text[:3000]}  
            ],
            temperature=0.5
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"PDF summarization failed: {e}"

tools = {
    "Calculator": Calculator,
    "Wikipedia": Wikipedia,
    "WebSearch": WebSearch,
    "SummarizePDF": SummarizePDF
}
