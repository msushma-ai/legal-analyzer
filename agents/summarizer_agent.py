from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def summarize_text(text):
    """
    Summarizes legal document content using an LLM.
    """
    llm = OpenAI(model_name="gpt-4", temperature=0.2)
    prompt = (
        "Summarize the following legal document concisely, focusing on parties, "
        "key clauses, obligations, and risks:\n\n"
        f"{text[:7000]}"
    )
    return llm(prompt)
