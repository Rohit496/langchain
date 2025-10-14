from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from dotenv import load_dotenv

load_dotenv()


# model
model = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

# parser
parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me 5 facts about {topic} \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

# chain
chain = template | model | parser

result = chain.invoke({"topic": "Artificial Intelligence"})
# print(result)

# Print each fact in the format 'fact1---> ...'
for key, value in result.items():
    print(f"{key}---> {value}")
