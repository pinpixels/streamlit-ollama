import requests
import streamlit as st
import json
import ollama
from typing import Dict, Generator

# Variables
OLLAMA_MODEL = "phi3:latest"


# Application title & caption
st.title("Chat with Ollama")
st.caption("This app assumes that you already have ollama available at default host (http://localhost:11434) on your machine with " + OLLAMA_MODEL + " model")

def ollama_generator(model_name: OLLAMA_MODEL, messages: Dict) -> Generator:
    stream = ollama.chat(
        model=model_name, messages=messages, stream=True)
    for chunk in stream:
        yield chunk['message']['content']


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)


    with st.chat_message("assistant"):
        response = st.write_stream(ollama_generator(
            OLLAMA_MODEL, st.session_state.messages))
    st.session_state.messages.append(
        {"role": "assistant", "content": response})
