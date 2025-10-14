from langchain_openai import ChatOpenAI

from dotenv import load_dotenv


load_dotenv()

# model
model = ChatOpenAI(model="gpt-4o", temperature=0.5, max_completion_tokens=10)

# invoke the model
result = model.invoke("What is the capital of India?")
print(result)
print(result.content)
