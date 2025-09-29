# ------------------------------<dynamic prompts> used saved prompt -----------------------------------------

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

# Initialize model
model = ChatGoogleGenerativeAI(model='models/gemini-2.5-pro')

st.header("Research Tool")

# dropdown code in streamlite
paper_input = st.selectbox("Select Research Paper Name", 
    ["Select...", 
     "Attention Is All You Need", 
     "BERT: Pre-training of Deep Bidirectional Transformers", 
     "GPT-3: Language Models are Few-Shot Learners", 
     "Diffusion Models Beat GANs on Image Synthesis"]
)
style_input = st.selectbox("Select Explanation Style", 
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)
length_input = st.selectbox("Select Explanation Length", 
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)


# used saved template(that is present in (save_template_for_reusable.py) file)
template=load_prompt('template.json')


# fill the placeholder
prompt=template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input

})

if st.button("Summarize"):
    result=model.invoke(prompt)
    st.write(result.content)
