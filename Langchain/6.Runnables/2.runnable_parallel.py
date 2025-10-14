from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()


# prompt template for twitter post generation
prompt1 = PromptTemplate(
    template="Generate a twitter post about {topic}", input_variables=["topic"]
)

# linkedIn post prompt template
prompt2 = PromptTemplate(
    template="Generate a LinkedIn post about {topic}", input_variables=["topic"]
)
model = ChatOpenAI()

# parser
parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        "twitter_post": RunnableSequence(prompt1, model, parser),
        "linkedin_post": RunnableSequence(prompt2, model, parser),
    }
)

# invoke the chain
result = parallel_chain.invoke({"topic": "AI"})
print(result)
print(result["twitter_post"])
print(result["linkedin_post"])
