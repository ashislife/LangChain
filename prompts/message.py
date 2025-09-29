from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='models/gemini-2.5-flash-lite')

# Initial messages
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me about extra LangChain features.")
]

# Invoke model
result = model.invoke(messages)

# Append AI response to chat history
messages.append(AIMessage(content=result.content))

for msg in messages:
    role = "System" if isinstance(msg, SystemMessage) else "User" if isinstance(msg, HumanMessage) else "AI"
    print(f"{role}: {msg.content}\n")