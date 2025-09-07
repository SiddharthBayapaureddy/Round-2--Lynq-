# Library Quick and Fast UI
import streamlit as st

# Backend tools
from pdf_reader import extract_text,summarize,interesting_facts,chat

st.title("PDF Analyzer")

# Selecting one of the PDFs
option = st.selectbox(
    "Choose a Topic" , 
    [
        "Black Holes" , "Extremophiles" , "Voynich Manuscript" , "Subglacial Lakes"
    ]
)

uploaded_file = st.file_uploader("Or upload your own PDF" , type="pdf")

path_dir = {
    "Black Holes" : "sample_pdfs/black_holes.pdf" , 
    "Extremophiles" : "sample_pdfs/extremophiles.pdf" ,
    "Voynich Manuscript" : "sample_pdfs/voynich_manuscript.pdf" , 
    "Subglacial Lakes" : "sample_pdfs/subglacial_lakes.pdf"
}

# Action to be performed on the PDF
action = st.radio(
    "Action",
    [   
        "Summarize" , "Interesting Facts" , "Ask Questions: Chatbot"
    ]
)

# Initialize session_state only once if not done so
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""

if st.button("Run"):

    # Taking text from the user uploaded file, or the sample ones accordingly 
    if uploaded_file is not None:
        st.session_state.pdf_text = extract_text(uploaded_file)
    else:
        st.session_state.pdf_text = extract_text(path_dir[option])
    
    # Clearing the history
    st.session_state.messages = []

# Summarizing Action Commands
if action == "Summarize" and st.session_state.pdf_text:
    st.write(summarize(st.session_state.pdf_text))

# Listing Interesting Facts Commands
if action == "Interesting Facts" and st.session_state.pdf_text:
    st.write(interesting_facts(st.session_state.pdf_text))

# Simple Chatbot for asking questions from the PDF
if action == "Ask Questions: Chatbot" and st.session_state.pdf_text:    
    st.subheader("Mini Chatbot: ")

    # Introducing only once, for the first time messages are recorded
    if not st.session_state.messages:
        chat.send_message(st.session_state.pdf_text)
        intro = chat.send_message(
            "Introduce yourself, and say that you're willing to assist about the information you received"
        )
        st.session_state.messages.append(f"Chatbot: {intro.text}")

    # Chat UI
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input("Ask about anything in the scope of PDF" , "")
        submitted = st.form_submit_button("Send")

    if submitted and user_input:
        st.session_state.messages.append(f"User: {user_input}")
        response = chat.send_message(user_input)
        st.session_state.messages.append(f"Chatbot: {response.text}")

    for msg in st.session_state.messages:
        st.write(msg)
