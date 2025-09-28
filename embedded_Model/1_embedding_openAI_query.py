from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv
load_dotenv()

embedding=OpenAIEmbeddings(model="",dimensions=32)

result=embedding.embed_query("Delhi is the Capital of India")


# result in vector 
print(str(result))


