# ---------------------------------------------> static prompts <--------------------------------------------------------------



from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Initialize model
model = ChatGoogleGenerativeAI(model='models/gemini-2.5-pro')

st.header("Research Tool")
user_input = st.text_input("Enter your Prompts")

if st.button("Summarize") and user_input:
    result = model.invoke(user_input)
    st.write(result.content)