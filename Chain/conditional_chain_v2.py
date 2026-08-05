from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch

load_dotenv()
model=ChatGroq(model="llama-3.3-70b-versatile")

parser = StrOutputParser()

# Step 1: Classify the review
classifier_prompt=PromptTemplate(
    template="""
    You are a movie review classifier.
    Classify the following review either:
    -positive
    -negative
    Return only one word: positive or negative
    
    review:{review}
    """,
    input_variables=["review"]
    
)
classifier_chain=classifier_prompt|model|parser

#Step 2
positive_prompt=PromptTemplate(
    template="Reply to this positive movie review in a friendly way:\n {review}",
    input_variables=["review"]
)
negative_prompt = PromptTemplate(
    template="Reply to this negative movie review by apologizing and offering help:\n{review}",
    input_variables=["review"]
)

positive_chain=positive_prompt|model|parser
negative_chain=negative_prompt|model|parser

review="The movie was absolutely fantastic.I loved every minute of it."

#Step3 :Sentiment
sentiment=classifier_chain.invoke({"review":review})
print("predicted sentiment",sentiment)

conditional_chain=RunnableBranch(
    (lambda x:x["sentiment"].strip().lower()=="Positive",positive_chain
    ),
    negative_chain
)

result=conditional_chain.invoke({
    "review":review,
    "sentiment":sentiment
})

print(result)