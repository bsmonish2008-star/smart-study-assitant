import streamlit as st
import ollama
from PyPDF2 import PdfReader

st.set_page_config(
    page_title="Smart Study Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Smart Study Assistant")
st.write("Your personal AI learning partner powered by Gemma 3")

uploaded_file = st.file_uploader(
    "Upload your study PDF",
    type=["pdf"]
)

if uploaded_file:
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    st.success("PDF uploaded successfully!")

    if st.button("Generate Summary"):
        with st.spinner("Gemma 3 is summarizing..."):
            response = ollama.chat(
                model="gemma3:1b",
                messages=[{
                    "role": "user",
                    "content": "Summarize these study notes in simple words:\n" + text[:12000]
                }]
            )
            st.subheader("📝 AI Summary")
            st.write(response["message"]["content"])

    if st.button("Generate Quiz"):
        with st.spinner("Creating questions..."):
            response = ollama.chat(
                model="gemma3:1b",
                messages=[{
                    "role": "user",
                    "content": "Create 5 multiple choice questions with answers from these notes:\n" + text[:12000]
                }]
            )
            st.subheader("🎯 Your AI Quiz")
            st.write(response["message"]["content"])

else:
    st.info("Upload your PDF to begin learning!")
