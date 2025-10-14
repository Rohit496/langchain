from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv


load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=32,
)

documents = [
    "Hello world",
    "LangChain is an open-source framework for developing applications powered by language models.",
    "Hugging Face is a company specializing in natural language processing.",
]


result = embeddings.embed_documents(documents)

print(result)
