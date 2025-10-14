from langchain_community.document_loaders import PyPDFLoader


# loader
loader = PyPDFLoader("Langchain/7.Document_Loader/dl-curriculum.pdf")

# load the document
documents = loader.load()

# print the document
print(documents)
# length of documents
print(len(documents))

# print the first document
print(documents[0])

# print the page content of the first document
print(documents[0].page_content)
# print the metadata of the first document
print(documents[0].metadata)
