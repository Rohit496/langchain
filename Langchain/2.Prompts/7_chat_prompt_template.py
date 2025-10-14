from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize the language model
model = ChatOpenAI(model_name="gpt-4o")

# Create the chat prompt template for translation
chat_template = ChatPromptTemplate(
    [
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}.",
        ),
        (
            "human",
            "{text}",
        ),
    ]
)

# Create the prompt with your input
prompt = chat_template.invoke(
    {
        "input_language": "English",
        "output_language": "Hindi",
        "text": "Hello, how are you?",
    }
)

print("Formatted prompt:")
print(prompt)
print("\n" + "=" * 50 + "\n")

# Actually get the translation by sending the prompt to the model
response = model.invoke(prompt)
print("Translation result:")
print(response.content)
