# Gemini Tools
from google import genai
from google.genai import types

# Loading env var
import os
from dotenv import load_dotenv
load_dotenv()

# Making an client instance
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash", # or "gemini-2-5-pro" for more crirical thinking
    contents="Introduce Yourself. Ask user what he/she want to know about.",

    # Pre-instructions on how the model behaves. Change is accordingly to preference
    config=types.GenerateContentConfig(
        system_instruction="Keep responses precise and cool"
    )
)
print(response.text)

# Chatbot
chat = client.chats.create(
    model = "gemini-2.5-flash",
    config= types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0),  # Disabling thinking ability for faster responses
        system_instruction="Keep responses short, precise and chatty."
    )
    )
user_input = input()

# Type exit to end chat
while(user_input!="exit"):
    output = chat.send_message(user_input)
    print(output.text)
    print()
    user_input = input()

print("Peace!")

