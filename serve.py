from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes
from dotenv import load_dotenv
load_dotenv()

## groq api key
groq_api_key = os.getenv("GROQ_API_KEY")
print(groq_api_key)

model = ChatGroq(api_key=groq_api_key, model="Gemma2-9b-It")
system_template = "Translate the following into '{language}'"

prompt= ChatPromptTemplate.from_messages([
    ("system",system_template),
    ("user","{text}")
])

parser = StrOutputParser()

## create the chain
chain = prompt | model | parser

## app definition
app = FastAPI(title="Translation API", description="An API to translate text using Groq model", version="1.0.0")
## add the route
add_routes(
    app,
    chain,
    path="/translate"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000, log_level="info")