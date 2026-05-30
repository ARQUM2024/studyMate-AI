# ============================================
# app.py — StudyMate AI
# ============================================

import streamlit as st
import os
import tempfile
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from rag import load_and_process_pdf, create_vectorstore, get_relevant_context
from prompts import SUMMARY_PROMPT, MCQ_PROMPT, QA_PROMPT, FLASHCARD_PROMPT, ELI5_PROMPT

# API Key load karo
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")s

# Groq LLM setup
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile",
    temperature=0.3
)

def ask_llm(prompt_text):
    """LLM se jawab lo"""
    try:
        response = llm.invoke([HumanMessage(content=prompt_text)])
        return response.content
    except Exception as e:
        return f"Error: {str(e)}"

# ---- Streamlit UI ----
st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚",
    layout="wide"
)

st.title("📚 StudyMate AI")
st.caption("Your Intelligent Study Assistant — Powered by Groq & LLaMA3")
st.divider()

# PDF Upload
uploaded_file = st.file_uploader(
    "📄 Upload your PDF (max 50MB)",
    type="pdf"
)

if uploaded_file:
    # PDF temp file mein save karo
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    st.success(f"✅ PDF uploaded: {uploaded_file.name}")

    # Process karo (sirf ek baar)
    with st.spinner("🔄 Processing your PDF..."):
        try:
            chunks = load_and_process_pdf(tmp_path)
            st.write(f"Chunks: {chunks}")
            if chunks:
                vectorstore = create_vectorstore(chunks)
                st.write(f"Vectorstore: {vectorstore}")
                full_text = " ".join([c.page_content for c in chunks[:10]])
                st.success(f"✅ PDF processed! ({len(chunks)} chunks created)")
            else:
                st.error("❌ TRY AGAIN.")
                st.stop()
        except Exception as e:
            st.error(f"❌ Exact Error: {str(e)}")
            st.stop()
    st.divider()

    # Feature Selection
    st.subheader("🎯 What do you want to do?")
    feature = st.selectbox(
        "Choose a feature:",
        ["📝 Summary", "❓ MCQ Generator",
         "💬 Ask a Question", "🃏 Flashcards", "🧒 Explain Simply"]
    )

    # ---- SUMMARY ----
    if feature == "📝 Summary":
        if st.button("Generate Summary", type="primary"):
            with st.spinner("Generating summary..."):
                prompt = SUMMARY_PROMPT.format(text=full_text)
                result = ask_llm(prompt)
                st.subheader("📋 Summary")
                st.write(result)

    # ---- MCQ ----
    elif feature == "❓ MCQ Generator":
        if st.button("Generate MCQs", type="primary"):
            with st.spinner("Generating MCQs..."):
                prompt = MCQ_PROMPT.format(text=full_text)
                result = ask_llm(prompt)
                st.subheader("❓ MCQs")
                st.write(result)

    # ---- Q&A ----
    elif feature == "💬 Ask a Question":
        question = st.text_input("🔍 Ask anything from your PDF:")
        if st.button("Get Answer", type="primary") and question:
            with st.spinner("Finding answer..."):
                context = get_relevant_context(vectorstore, question)
                prompt = QA_PROMPT.format(
                    context=context,
                    question=question
                )
                result = ask_llm(prompt)
                st.subheader("💡 Answer")
                st.write(result)

    # ---- FLASHCARDS ----
    elif feature == "🃏 Flashcards":
        if st.button("Generate Flashcards", type="primary"):
            with st.spinner("Creating flashcards..."):
                prompt = FLASHCARD_PROMPT.format(text=full_text)
                result = ask_llm(prompt)
                st.subheader("🃏 Flashcards")
                st.write(result)

    # ---- ELI5 ----
    elif feature == "🧒 Explain Simply":
        concept = st.text_input("Enter a concept to explain simply:")
        if st.button("Explain!", type="primary") and concept:
            with st.spinner("Explaining..."):
                prompt = ELI5_PROMPT.format(concept=concept)
                result = ask_llm(prompt)
                st.subheader("🧒 Simple Explanation")
                st.write(result)

else:
    st.info("👆 Please upload a PDF to get started!")