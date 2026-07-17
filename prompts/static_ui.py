from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
model=ChatGroq(model='llama-3.1-8b-instant')

st.header("Research tool")
user_input = st.text_input("Enter your prompt")
if st.button("Summarize"):
    #Model invoke -->with user prompt
    
    result=model.invoke(user_input)
    
    #Show result-->st.write
    st.write(result.content)