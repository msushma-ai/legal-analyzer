from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

def create_vector_store(text):
    """
    Splits text into chunks and creates a Chroma vector store.
    """
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.create_documents([text])
    embeddings = OpenAIEmbeddings()
    db = Chroma.from_documents(docs, embedding=embeddings)
    return db
