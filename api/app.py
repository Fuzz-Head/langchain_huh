from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os 
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
os.environ["LANGSMITH_TRACING"]="true"
## If this is commented how is it tracking?
## Maybe because it is already tracked and is a part of it.
# os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

app=FastAPI(
    title="Langchain server",
    version="1.0",
    description="A simple API server"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)
model=ChatOpenAI()
llm=Ollama(model="llama3:8b")

prompt1=ChatPromptTemplate.from_template("Write me a thought about {topic} with 15 words")
prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} with 80 words")

add_routes(
    app,
    prompt1|model,
    path="/thought"
)

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)