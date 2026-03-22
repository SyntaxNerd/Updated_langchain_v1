import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

from langchain.agents import create_agent
from langchain_groq.chat_models import ChatGroq
from langchain.tools import tool

model = ChatGroq(
    model = "openai/gpt-oss-120b",
    temperature = 0,
    max_tokens = None
)

@tool
def get_weather(location: str) -> str:
    """
    Returns the current weather of the location given
    """
    return f"The current weather in {location} is Overcast"

agent = create_agent(
    model = model,
    tools = [get_weather],
    system_prompt = "You are a helpful assistant."
)

messages = {"messages": [{"role": "user", "content": "What is the current weather in London?"}]}
response = agent.invoke(messages)
print(response["messages"][-1].content)