# without chat history - basic chatbot

from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()


model = ChatOpenAI(model_name="gpt-4o")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    response = model.invoke(user_input)
    print(f"Chatbot: {response.content}")
