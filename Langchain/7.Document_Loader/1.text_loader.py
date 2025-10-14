from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI


from dotenv import load_dotenv


load_dotenv()


# model
model = ChatOpenAI()

# prompt template
prompt = PromptTemplate(
    template="Write a short summary of the following text:\n\n{text}",
    input_variables=["text"],
)

# parser
parser = StrOutputParser()


loader = TextLoader("Langchain/7.Document_Loader/cricket.txt", encoding="utf8")

# load the document
documents = loader.load()

# print the document
# print(documents)

# # type of documents
# print(type(documents))

# # print the first document
# print(documents[0])

# # print the page content of the first document
# print(documents[0].page_content)

# # print the metadata of the first document
# print(documents[0].metadata)


# chain
chain = prompt | model | parser
# invoke the chain
result = chain.invoke({"text": documents[0].page_content})
print(result)
