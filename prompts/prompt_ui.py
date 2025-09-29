# import streamlit as st
# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# # Load API key
# load_dotenv()

# # Sidebar settings
# st.set_page_config(page_title="Research Tool", page_icon="🔎", layout="wide")
# st.sidebar.title("⚙️ Settings")

# # Model selection (Flash = faster, Pro = smarter)
# model_choice = st.sidebar.radio(
#     "Choose Model",
#     ["gemini-1.5-flash (fast)", "gemini-2.5-pro (accurate)"]
# )

# # Initialize model
# model = ChatGoogleGenerativeAI(
#     model="models/gemini-2.5-pro" if "flash" in model_choice else "models/gemini-2.5-pro"
# )

# # Clear chat button
# if st.sidebar.button("🧹 Clear Chat"):
#     st.session_state.history = []

# # Page header
# st.title("🔎 Research Assistant")
# st.markdown("Ask questions, get **summaries, insights, or explanations** instantly.")

# # Initialize history
# if "history" not in st.session_state:
#     st.session_state.history = []

# # Chat display
# for msg in st.session_state.history:
#     if msg["role"] == "user":
#         st.markdown(f"""
#         <div style='text-align: right; background-color: #DCF8C6; padding: 10px; border-radius: 10px; margin: 5px;'>
#             🧑 <b>You:</b> {msg["content"]}
#         </div>
#         """, unsafe_allow_html=True)
#     else:
#         st.markdown(f"""
#         <div style='text-align: left; background-color: #E6E6FA; padding: 10px; border-radius: 10px; margin: 5px;'>
#             🤖 <b>AI:</b> {msg["content"]}
#         </div>
#         """, unsafe_allow_html=True)

# # Input at bottom
# st.markdown("---")
# user_input = st.text_input("💬 Enter your prompt:", key="input", placeholder="Type your question here...")

# # Streaming response
# if st.button("🚀 Send") and user_input:
#     st.session_state.history.append({"role": "user", "content": user_input})

#     response_box = st.empty()
#     answer = ""

#     for chunk in model.stream(user_input):
#         answer += chunk.content or ""
#         response_box.markdown(f"""
#         <div style='text-align: left; background-color: #E6E6FA; padding: 10px; border-radius: 10px; margin: 5px;'>
#             🤖 <b>AI:</b> {answer}
#         </div>
#         """, unsafe_allow_html=True)

#     st.session_state.history.append({"role": "assistant", "content": answer})



# ---------------------------------------------><--------------------------------------------------------------


# static prompts 
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






