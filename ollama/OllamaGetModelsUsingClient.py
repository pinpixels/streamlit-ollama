import streamlit as st
from ollama import Client
from typing import Dict, Generator

OLLAMA_HOST = 'http://localhost:11434'
client= Client(host= OLLAMA_HOST)

def ollama_generator(model_name: str, messages: Dict) -> Generator:
    stream = client.chat(
        model=model_name, messages=messages, stream=True)
    for chunk in stream:
        yield chunk['message']['content']


st.title("Ollama Configured Client")
st.caption("Ollama Host: " + OLLAMA_HOST)
st.caption("This app uses Ollama client to configure the host instead of default Ollama instance. Pulls a list of models available at the configured Ollama instance and loads into a select box.")
st.divider()

if "selected_model" not in st.session_state:
    st.session_state.selected_model = ""
    
if "messages" not in st.session_state:
    st.session_state.messages = []

st.session_state.selected_model = st.selectbox(
    "Please select the model:", [model["name"] for model in client.list()["models"]])

