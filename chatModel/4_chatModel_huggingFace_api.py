from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint

from dotenv import load_dotenv


load_dotenv()


# repo id-->which model you want to use 
llm=HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-V3.1-Terminus',
    task='text-generation'
)
model=ChatHuggingFace(llm=llm)

result=model.invoke("What is the Capital of India?")

print(result.content)



