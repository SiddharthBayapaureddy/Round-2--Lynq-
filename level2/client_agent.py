# For asnyic and await tools
import asyncio
from fastmcp import Client

# Gemini Tools
from google import genai
from google.genai import types


import os
from dotenv import load_dotenv
load_dotenv("../.env")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


user_input = input("Ask anything about weather: (Type 'exit' to quit)\n")   
user_city = ""


response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_input,

    config=types.GenerateContentConfig(
        system_instruction="Extract the city name from the input, and return it as output. No city name, return 'error'." ,
        thinking_config=types.ThinkingConfig(thinking_budget=0)
    )
)

user_city = response.text

if(user_input == "exit"):
    user_city = "none"

async def main():
    client = Client("weather_mcp.py")
    
    async with client:

        # Handling exit case
        if(user_city == "none"):
            return

        # Calling the tool
        result = await client.call_tool("get_weather", {"city": user_city})
        
        print(result.data)

if __name__ == "__main__":
    asyncio.run(main())
