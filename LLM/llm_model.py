import os
from dotenv import load_dotenv 
from langchain_google_genai import ChatGoogleGenerativeAI # Switch to Chat class

# Load environment variables from .env file
load_dotenv()

# Initialize the model using a newer, supported version (e.g., gemini-3.5-flash)
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash"
)

# Invoke the model
result = llm.invoke("What is the Capital of Bangladesh")

# Print the result (using .content since Chat models return an AIMessage object)
print(result)