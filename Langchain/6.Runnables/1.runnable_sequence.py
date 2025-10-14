from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence

load_dotenv()

# prompt template for joke generation
prompt1 = PromptTemplate(
    template="Tell me a joke about {topic}", input_variables=["topic"]
)


# describe the joke in prompt2
prompt2 = PromptTemplate(
    template="Describe the joke about {text}", input_variables=["text"]
)

model = ChatOpenAI()

# parser
parser = StrOutputParser()

# chain
chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

print(chain.invoke({"topic": "AI"}))


# # Generate the joke
# joke = prompt1 | model | parser
# joke_text = joke.invoke({"topic": "AI"})
# print("Joke:")
# print(joke_text)

# # Generate the explanation
# explanation = prompt2 | model | parser
# explanation_text = explanation.invoke({"text": joke_text})
# print("\nExplanation:")
# print(explanation_text)
