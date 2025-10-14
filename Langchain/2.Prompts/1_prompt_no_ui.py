from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
user_input = input("Enter your prompt here:\n")

response = llm.invoke(user_input)  # Call the model with user input

print(response.content)  # Display the content of the response
