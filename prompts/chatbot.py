#-----------------> esko previous code yaad nhi rahta , matlab chat histroy nhi rahti es code me <------------------ 
# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()


# model = ChatGoogleGenerativeAI(model='models/gemma-3-27b-it')

# while True:
#     user_input=input('You: ')
#     if user_input=='exit':
#         break
#     result=model.invoke(user_input)
#     print('AI: ',result.content)
    










# # --------------------<save also chat history<------------------------------
# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()


# model = ChatGoogleGenerativeAI(model='models/gemma-3-27b-it')

# chat_history=[]

# while True:
#     user_input=input('You: ')
    
#     # append the chat history of user ki dubara us chat pr kaam ho sake 
#     chat_history.append(user_input) 

#     if user_input=='exit':
#         break
#     result=model.invoke(chat_history)

#     # also append the chat history of AI ki dubara us chat pr kaam ho sake 
#     chat_history.append(result.content)
#     print('AI: ',result.content)


# # BUT es print me dikkat hai ki hi pura history print to kr dega pr ye pta nhi chalega ki AI ka hai use ne bha hai wo msg kon sa hai(esko solve karne ke liye (message) use hota hai )
# print(chat_history)




# ---------------<solve the chat history problem<------------------------------
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


model = ChatGoogleGenerativeAI(model='models/gemini-2.5-flash-lite')

chat_history=[
    SystemMessage(content="You are a helpfull AI assistant")   
]

while True:
    user_input=input('You: ')
    
    # append the chat history of user ki dubara us chat pr kaam ho sake or ye message labelled ho rha hai ki human ne kiya hai msg 
    chat_history.append(HumanMessage(content=user_input)) 

    if user_input=='exit':
        break
    result=model.invoke(chat_history)

    # also append the chat history of AI ki dubara us chat pr kaam ho sake 
    chat_history.append(AIMessage(content=result.content))
    print('AI: ',result.content)

print(chat_history)
