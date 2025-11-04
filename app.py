import streamlit as st
from agents.reader_agent import extract_text_from_pdf
from vector_store.chromadb_utils import create_vector_store
from agents.summarizer_agent import summarize_text

st.set_page_config(page_title="Legal Document Analyzer", page_icon="📚")
st.title("Legal Document Analyzer (Multi-Agent Paralegal Bot)")

uploaded_file = st.file_uploader("Upload Legal PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting text..."):
        text = extract_text_from_pdf(uploaded_file)
    st.success("Text extracted successfully!")

    with st.spinner("Creating vector store..."):
        db = create_vector_store(text)
    st.success("Vector store created!")

    if st.button("Generate Summary"):
        with st.spinner("Generating summary..."):
            summary = summarize_text(text)
        st.subheader("Summary")
        st.write(summary)
