from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

from dotenv import load_dotenv

load_dotenv()


# model
model = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")


# schemas
response_schemas = [
    ResponseSchema(name="fact1", description="this is fact1"),
    ResponseSchema(name="fact2", description="this is fact2"),
    ResponseSchema(name="fact3", description="this is fact3"),
]

# parser
parser = StructuredOutputParser.from_response_schemas(response_schemas)

template = PromptTemplate(
    template="Give me 5 facts about {topic} \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

# chain
chain = template | model | parser
result = chain.invoke({"topic": "Artificial Intelligence"})
print(
    result
)  # {'fact1': 'Fact about AI 1', 'fact2': 'Fact about AI 2', 'fact3': 'Fact about AI 3'}
