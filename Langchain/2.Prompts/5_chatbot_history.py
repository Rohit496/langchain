from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()


model = ChatOpenAI(model_name="gpt-4o")

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    response = model.invoke(chat_history)
    chat_history.append(response.content)
    print(f"Chatbot: {response.content}")

# Note: The chat history is maintained as a simple list of messages.
# print the entire chat history for context
print("Chat History:", chat_history)
