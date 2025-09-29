# check which model are available in gemini 
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("AIzaSyD2kphb--O0ZHX1NRBxiSqyay_ehKm4JCU"))
for m in client.models.list():
    print(m.name)



# --------------------<>-------------------------------
# from langchain_google_genai import ChatGoogleGenerativeAI

# from dotenv import load_dotenv
# load_dotenv()

# model=ChatGoogleGenerativeAI(model='models/gemini-2.5-pro')
# result=model.invoke("Waht is the Capital of India ?")

# print(result.content)



