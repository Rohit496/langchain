from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()


# model
model = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")


# 1st prompt -> detailed report
template1 = PromptTemplate(
    template="""Write a detailed report on {topic}""", input_variables=["topic"]
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template="""Write a 5 line summary on the following text. /n {text}""",
    input_variables=["text"],
)

# parser
parser = StrOutputParser()

# chain
chain = template1 | model | parser | template2 | model | parser
response = chain.invoke({"topic": "Artificial Intelligence"})
print(response)
