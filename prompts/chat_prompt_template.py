# ---------------<not run bc of version mismatch >-------------------
from langchain_core.prompts import ChatMessagePromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage

# Chat template using list of dicts
chat_template = ChatMessagePromptTemplate(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessage(content="{query}")
    ]
)

# Example chat history as ChatMessage objects
chat_history = [
    HumanMessage(content="Hi, I need help with my order."),
    HumanMessage(content="My order ID is 12345.")
]

# Create prompt
prompt = chat_template.format_prompt({
    "chat_history": chat_history,
    "query": "Where is my refund?"
})

print(prompt.to_messages())


