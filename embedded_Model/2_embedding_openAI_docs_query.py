# -------------->paid user api------------------>
from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv
load_dotenv()

embedding=OpenAIEmbeddings(model="",dimensions=32)


# embedding more than one query
documents=[
    "Delhi is the Capital of India "
    "Kolkata is the capital of west Bengal"
    "paris is the capital of France"
]

result=embedding.embed_documents(documents)


# result in vector 
print(str(result))