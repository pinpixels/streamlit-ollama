import streamlit as st

st.title("Hello World")
st.caption("Streamlit Example")

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
    
with st.chat_message("user"):
 st.write("Hello 👋")
