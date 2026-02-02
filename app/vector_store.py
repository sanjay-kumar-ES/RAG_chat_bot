
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

def create_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma.from_documents(chunks, embeddings, persist_directory="./db")
    vectordb.persist()

    return vectordb
