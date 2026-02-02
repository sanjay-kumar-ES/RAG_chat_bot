
from fastapi import FastAPI
from .rag_pipeline import build_qa
from .vector_store import create_vectorstore
from .embeddings import load_docs


app = FastAPI()

chunks = load_docs("data/resume.pdf")
vectordb = create_vectorstore(chunks)
qa = build_qa(vectordb)

@app.get("/ask")
def ask(q: str):
    result = qa({"query": q})
    return {"answer": result["result"]}
