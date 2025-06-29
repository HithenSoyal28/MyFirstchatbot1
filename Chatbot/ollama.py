from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
#from langchain_ollama import OllamaLLM


import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Create chatbot prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please provide more detailed responses."),
    ("user", "Question: {question}")
])

# Streamlit interface
st.title("Langchain Demo with Llama2 via Ollama")
input_text = st.text_input("Search the topic you want")

# LLM initialization (Ollama)
llm = Ollama(model="llama2")

output_parser = StrOutputParser()

# Chain
chain = prompt | llm | output_parser

if input_text:
    result = chain.invoke({"question": input_text})
    st.write(result)
