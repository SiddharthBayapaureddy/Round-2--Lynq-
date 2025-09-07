# PDF Reader
from pypdf import PdfReader

# Gemini Tools
from google import genai
from google.genai import types

# Os tools
import os
from dotenv import load_dotenv
load_dotenv()


# Extracting contents of the PDF
def extract_text(path: str):

    # PDF Reader instance
    pdf_reader = PdfReader(path)

    # Extracting text from the PDF
    extracted_text = ''''''

    for i,page in enumerate(pdf_reader.pages):
        text = page.extract_text()

        if text is not None:
            extracted_text += text
            extracted_text += '\n\n'

    #print(extracted_text)
    return extracted_text

#************************************************************************************************************************************

# Using Gemini to analyze and summarize the PDF
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def summarize(input_txt: str):

    response = client.models.generate_content(
        model="gemini-2.5-pro" , # Better for thinking, and large input
        contents=input_txt,

        config=types.GenerateContentConfig(
            system_instruction="Summarize only core ideas, keep it concise, clear, and no extra info. Add bullets."
        )

    )

    return response.text

#************************************************************************************************************************************

def interesting_facts(input_txt: str):

    response = client.models.generate_content(
        model="gemini-2.5-flash" , 
        contents=input_txt,

        config=types.GenerateContentConfig(
            system_instruction="Generate 3-4 interesting facts on this text. Use bullets"
        )

    )

    return response.text

#************************************************************************************************************************************

# Chatbot instance

chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0), 
        system_instruction="You're a chatbot, and you'll only answer questions in the scope of the first text you receive. No extra, keep it short and precise"
    )
)
