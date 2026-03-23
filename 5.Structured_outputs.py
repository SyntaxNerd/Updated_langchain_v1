import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

from langchain.agents import create_agent
from langchain_groq.chat_models import ChatGroq
from langchain.tools import tool
from langchain.messages import SystemMessage, HumanMessage
from pydantic import BaseModel, Field

model = ChatGroq(
    model = "openai/gpt-oss-120b",
    temperature = 0,
    max_tokens = None
)

class Movie(BaseModel):
    title:str = Field(description = "The title of the movie")
    year:int = Field(description = "Release date of the movie")
    director:str = Field(description = "The director of the movie")
    ratings:float = Field(description = "The ratings of the movie out of 10")

agent = create_agent(
    model = model,
    tools = [],
    response_format = Movie, # Pydantic class fed to the agent
    system_prompt = "You are a helpful assistant that helps to fetch movie details"
)

messages = {
    "messages": [{"role": "user", "content": "Provide me the details of the movie Interstellar"}]
}
response = agent.invoke(messages)
print(response["messages"][-1].content)