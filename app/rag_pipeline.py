from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

def build_qa(vectordb):

    llm = Ollama(
        model="llama3.1:8b",
        temperature=0
    )

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectordb.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True
    )

    return qa
