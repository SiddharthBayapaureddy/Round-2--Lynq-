# **Round-2 (LYNQ)**

### Used Google's Gemini API 

## **1. Level-I**
### llm_call.py : 
#### Run the file to talk with Gemini, with a simple CLI Chatbot. 
sample input: "Tell me about Elephants" , "What is a comet?" , etc

### pdf_reader.py : *Not required to run*
#### Simple PDF Text Extractor and Analyzer using pypdf and Gemini. Test the user-defined functions by modifying the code. The file acts like a simple backend for the Frontend UI. 

### ui_interface.py: *Frontend Interface*
#### A simple interface to upload PDF files and perform pre-defined actions on them.

#### To run, type in the following command in the terminal of level1 directory
#### *streamlit run ui_interface.py*

#### It should open a localhost live session that can be accessed from a default browser by ctrl clicking the address mentioned in terminal. Test the features available.
#### I've used the Streamlit library, which is a free, simple python library that help create a working frontend within seconds. 
#### I've included some sample PDFs to test the bot, you can also upload your own PDFs to test the bot


## **2. Level-II**

### weather_mcp.py :
#### Contains the FastMCP server, and standard input/output tools defined. 

### client_agent.py : 
#### It calls the MCP server tool i.e., "get_weather", to return the climate details accordingly to user input. Proper exception handling is present. 

### To run the agent, follow the steps: 
### 1. Type this command in the terminal of level2 directory
#### *python weather_mcp.py*
### This gets the server up and running, and ready for the client to make calls. 
### **Don't close the terminal. Keep it running in the background**

### 2. Open a new terminal fn the same directory, and type in the following command:
#### *python client_agent.py*
### This will get the agent running, and you can interact with the bot in the CLI. 

### Sample IO: 
#### *What's the weather in hyderabad?*
#### *Is it hot in chennai rn?*
