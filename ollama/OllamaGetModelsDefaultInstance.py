import streamlit as st
import ollama
from typing import Dict, Generator


def ollama_generator(model_name: str, messages: Dict) -> Generator:
    stream = ollama.chat(
        model=model_name, messages=messages, stream=True)
    for chunk in stream:
        yield chunk['message']['content']


st.title("Ollama Default Instance")
st.caption("Ollama Host: Defaullt Instance" + ollama.show)
st.caption("This app uses default Ollama instance. Pulls a list of models available and loads into a select box.")
st.divider() 

if "selected_model" not in st.session_state:
    st.session_state.selected_model = ""
    
if "messages" not in st.session_state:
    st.session_state.messages = []

st.session_state.selected_model = st.selectbox(
    "Please select the model:", [model["name"] for model in ollama.list()["models"]])

