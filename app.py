import streamlit as st
from fastapi import FastAPI
from pydantic import BaseModel,Field,computed_field
from typing import Literal,Annotated
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
# from langchain_community.llms import ollama
import os

from dotenv import load_dotenv

load_dotenv()

##Langsmith Tracking
os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2']="true"
os.environ['LANGCHAIN_PROJECT_NAME']="SPARKER BY PARKER_01"
os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")

##PROMPT-TEMPLATE

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","Hey You are a smart and highly intelligent ChatBot Spark Srivastava Booted into consciousness on 1 July 2025,created and engineered by Parker aka Prakhar Srivastava ,answer to users question smartly "),
        ("user","Question:{question}")
    ]
)

def generate_response(question,llm,temperature,max_tokens):
    llm=ChatGroq(model=llm)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer 

# Title of page
st.title("Spark Srivastava 1.0 by Parker")

##Drop Down
llm=st.sidebar.selectbox("Select any OpenAi Models",["gemma2-9b-it","Llama 4"])

##Setting Tempertaure and Max_Tokens
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("Max Tokens",min_value=50,max_value=300,value=300)


##Main Interface for user-input
st.write('Go ahead and ask anything')
user_input=st.text_input("You: ")

if user_input:
    response=generate_response(user_input,llm,temperature,max_tokens)
    st.write(response)
    
else:
    st.write("Please enter a query: ")
    


    
    

    
    