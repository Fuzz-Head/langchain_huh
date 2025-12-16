from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langsmith import traceable

import streamlit as st 
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## LangSmith tracking
os.environ["LANGCHAIN_TRACKING_V2"]="true"
os.environ["LANGSMITH_TRACING"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt template 

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the user queries briefly"),
        ("user","QUeestion:{question}")
    ]
)

## Streamlit framework

st.title('Langchain Demo with OPENAI API')
input_text=st.text_input("Search the topic you want")

# openAI LLM
llm=ChatOpenAI(model="gpt-5-nano")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

## need these modifications so as to keep it to the original
@traceable
def get_output_openai(question):
    if question:
        response = chain.invoke({'question': question})
        st.write(response)
    else:
        st.info("Please enter a question")

# Call function with input
get_output_openai(input_text)
