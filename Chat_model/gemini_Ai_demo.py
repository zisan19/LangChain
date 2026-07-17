from langchain_google_genai import ChatGoogleGenerativeAI # Switch to Chat class
from dotenv import load_dotenv
load_dotenv()
llm = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash'
)
result = llm.invoke("What is the Capital of Bangladesh")
print(result.content)
