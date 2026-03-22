import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

from langchain.agents import create_agent
from langchain_groq.chat_models import ChatGroq

model = ChatGroq(
    model = "openai/gpt-oss-120b",
    temperature = 0,
    max_tokens = None
)

agent = create_agent(
    model = model,
    tools = [],
    system_prompt = "You are a helpful assistant."
)

messages = {"messages": [{"role": "user", "content": "Why do parrots have colorful feathers?"}]}
for chunk in agent.stream(messages, stream_mode = "updates", version = "v2"):
    if chunk["type"] == "updates":
        for step, data in chunk["data"].items():
            print(f"Content: {data["messages"][-1].content}")