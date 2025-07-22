import os
import psycopg2
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.utilities import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from dotenv import load_dotenv

load_dotenv()

POSTGRES_URL = os.getenv("POSTGRES_URL") 
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

db = SQLDatabase.from_uri(POSTGRES_URL) # type: ignore

llm = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY) # type: ignore

db_toolkit = SQLDatabaseToolkit(llm=llm, db=db)

tools = db_toolkit.get_tools()

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True) # type: ignore

def query_agent(input_text):
    return agent.run(input_text)
