from langchain_groq import ChatGroq
from dotenv import load_dotenv 

load_dotenv()
model=ChatGroq(model="llama-3.1-8b-instant")

#chatbot 
while True:
    user_input = input('You :')

    #chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(user_input)
    print("AI : ", result.content)
