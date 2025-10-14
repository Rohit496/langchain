from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()


# model
model = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")


# pydantic model for person name, age and country
class Person(BaseModel):
    name: str = Field(..., description="Name of the person")
    age: int = Field(gt=18, description="Age of the person")
    country: str = Field(..., description="Country of the person")


# parser
parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate the name, age and city of a fictional {place} person \n {format_instruction}",
    input_variables=["place"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

# chain
chain = template | model | parser
result = chain.invoke({"place": "India"})
print(result)
