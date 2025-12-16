import requests
import streamlit as st
from langsmith import traceable

@traceable
def get_openai_response(input_text):
    response=requests.post("http://localhost:8000/thought/invoke",
                           json={'input':{'topic':input_text}})
    
    return response.json()['output']['content']

@traceable
def get_ollama_response(input_text):
    response=requests.post("http://localhost:8000/poem/invoke",
                           json={'input':{'topic':input_text}})
    
    return response.json()['output']

## streamlit framework 

st.title('Langchain Demo with LLAMA3 API')
input_text=st.text_input("Write a thought on")
input_text1=st.text_input("Write a poem on")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))