# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv

load_dotenv()


# Hugging Face llm
# llm = HuggingFaceEndpoint(
#     repo_id="deepseek-ai/DeepSeek-V3.2-Exp",
#     task="text-generation",
# )

# model
model = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")


# 1st prompt -> detailed report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}", input_variables=["topic"]
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text. /n {text}",
    input_variables=["text"],
)

prompt1 = template1.format(topic="Artificial Intelligence")
response1 = model.invoke(prompt1)


prompt2 = template2.format(text=response1.content)
response2 = model.invoke(prompt2)

print(response2.content)
