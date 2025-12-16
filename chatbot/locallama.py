from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from langsmith import traceable

import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework 

st.title('Langchain Demo with LLAMA3 API')
input_text=st.text_input("Search your desired topic")

## ollama LLAMA2 LLM 
llm=Ollama(model="llama3:8b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

@traceable
def get_output_ollama(question):
    if question:
        response = chain.invoke({'question': question})
        st.write(response)
    else:
        st.info("Please enter a question")

get_output_ollama(input_text)