from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import (
    RunnableSequence,
    RunnableParallel,
    RunnablePassthrough,
)

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

# joke generation chain
joke_generation_chain = RunnableSequence(prompt1, model, parser)

# parallel chain to run the joke generation and joke
parallel_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "explanation": RunnableSequence(prompt2, model, parser),
    }
)

# full chain
final_chain = RunnableSequence(joke_generation_chain, parallel_chain)

result = final_chain.invoke({"topic": "AI"})

# print the joke name
print("\nJoke:")
print(result["joke"])
# print the explanation
print("\nExplanation:")
print(result["explanation"])
