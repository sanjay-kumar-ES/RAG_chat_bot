
import streamlit as st
import requests

st.title("Resume Q&A Bot")

q = st.text_input("Ask something about my resume")

if q:
    r = requests.get(f"http://localhost:8000/ask?q={q}")
    st.write(r.json()["answer"])
