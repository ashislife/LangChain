from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()

# tempereture -->creative parameter ,(max_completion_tokens==no of words )
model=ChatOpenAI(model='gpt-4',temperature=1.5,max_completion_tokens=10)

result=model.invoke("What is the capital of india?")
print(result.content)

