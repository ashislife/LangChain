# -----------------------------<not run bc of version mismatch>--------------------
from langchain_core.prompts import ChatMessagePromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Load chat history as ChatMessage objects
chat_history = []
with open('chathistory.txt') as f:
    for line in f:
        chat_history.append(HumanMessage(content=line.strip()))  # ya AIMessage, depend on who sent it

# Create chat template
chat_template = ChatMessagePromptTemplate.from_messages([
    SystemMessage(content="You are a helpful assistant."),
    MessagesPlaceholder(variable_name='chat_history'),
    HumanMessage(content="{query}")
])

# Create prompt
prompt = chat_template.format_prompt({
    'chat_history': chat_history,
    'query': "Where is my refund?"
})

print(prompt.to_messages())
