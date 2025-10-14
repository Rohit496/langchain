from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()


# model
model = ChatOpenAI(temperature=0, model_name="gpt-4o")


# prompt
prompt = PromptTemplate(
    template="""Write a detailed report on {topic}""", input_variables=["topic"]
)

# parser
parser = StrOutputParser()

# chain
chain = prompt | model | parser

# invoke
response = chain.invoke({"topic": "Salesforce"})

# visualize the chain
chain.get_graph().print_ascii()
