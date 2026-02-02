 RAG Chatbot (Local LLM + LangChain)

A fully offline **Retrieval-Augmented Generation (RAG)** chatbot that answers questions from my resume and documents using embeddings + vector search + a local LLM.

This project demonstrates :
- LLM integration
- Vector databases
- RAG pipelines
- Backend APIs
- Local GPU inference
- Production-style architecture


To run program first install all requirements (pip install -r requirements.txt)
instll ollama (ollama pull llama3.1:8b)
add you pdf @ (eg:data/resume.pdf)
python run.py

