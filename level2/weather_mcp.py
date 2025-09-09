# Building a Mini MCP Tool stdio server 

# FastMCP 2.0 (Actively Maintained Version)
from fastmcp import FastMCP

# For requesting an API Call
import requests

import os
from dotenv import load_dotenv
load_dotenv("../.env")
API_KEY = os.getenv("OPENWEATHER_API_KEY")


# Creating an FastMCP instance
mcp = FastMCP("weather-mcp")


@mcp.tool()
def get_weather(city: str) -> str:


    # URL for Requesting Open Weather API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    # Converting into JSON for better readability
    data = response.json()

    # Handling Error:200 (Common)
    if response.status_code != 200:
        return f"Error fetching weather for {city}: {data.get('message', 'Unknown error')}"

    # Getting required data
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    return f"It's {description}, {temp}°C in {city}."

    

if __name__ == "__main__":
    mcp.run()  # stdio mode
