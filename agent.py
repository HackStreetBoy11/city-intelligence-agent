# agent.py
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain.agents import create_agent

from tools import get_weather, web_search

load_dotenv()

llm = ChatMistralAI(
    model="mistral-small-2506"
)

agent = create_agent(
    llm,
    tools=[get_weather, web_search],
    system_prompt="""
    You are a professional city intelligence assistant.

    You help users with:
    - weather
    - city information
    - latest news
    - internet search
    """
)

def run_agent(query: str):

    result = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": query
            }
        ]
    })

    return result["messages"][-1].content