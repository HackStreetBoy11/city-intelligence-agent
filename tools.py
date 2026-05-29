# tools.py

from dotenv import load_dotenv
from tavily import TavilyClient
from langchain.tools import tool

import os
import requests

load_dotenv()

# WEATHER TOOL

@tool
def get_weather(CITY_NAME: str) -> str:
    """Get current weather of a city"""

    API_KEY = os.getenv("OPENWEATHER_API_KEY")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if str(data.get("cod")) != "200":
        return f"Error: {data.get('message')}"

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    return f"""
    🌦 Weather in {CITY_NAME}

    Temperature: {temp}°C
    Condition: {desc}
    """


# TAVILY SEARCH TOOL

tavily_client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

@tool
def web_search(query: str) -> str:
    """Search latest information from internet"""

    response = tavily_client.search(
        query=query,
        search_depth="basic",
        max_results=3
    )

    results = response.get("results", [])

    if not results:
        return "No results found."

    final_answer = ""

    for idx, result in enumerate(results, start=1):

        final_answer += f"""
### Result {idx}

🔹 Title: {result['title']}

🔹 URL: {result['url']}

🔹 Content:
{result['content']}

---
"""

    return final_answer