#LANGCHAIN_API_KEY = "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"
#LANGSMITH_TRACING=true
#LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
#LANGSMITH_PROJECT="Tutorial1Hindi"
OPENAI_API_KEY="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"

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# envt variable call

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langsmith tracking

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

## create chatbot

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant, please prvide more response to the user quesry"),
        ("user","Question:{question}")
    ]
)

# streamlit framework

st.title("Langchain Demo With Open AI API")
input_text=st.text_input("Search the topic you want")

# open AI LLM call

llm=ChatOpenAI(model = "gpt-3.5-turbo")
output_parser=StrOutputParser()

## chain
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question'}))