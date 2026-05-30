# ============================================
# rag.py — StudyMate AI
# ============================================

import os
import tempfile
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def load_and_process_pdf(pdf_path):
    """PDF load karo aur chunks banao"""
    try:
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

        if not documents:
            print("ERROR: PDF empty hai ya read nahi ho saki")
            return None

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        chunks = splitter.split_documents(documents)
        print(f"SUCCESS: {len(chunks)} chunks bane")
        return chunks

    except Exception as e:
        print(f"PDF ERROR: {str(e)}")
        return None

def create_vectorstore(chunks):
    """ChromaDB mein embeddings store karo"""
    try:
        embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )
        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory="./chroma_db"
        )
        print("SUCCESS: Vectorstore bana gaya")
        return vectorstore

    except Exception as e:
        print(f"VECTORSTORE ERROR: {str(e)}")
        return None

def get_relevant_context(vectorstore, question, k=3):
    """Question ke liye relevant chunks dhundo"""
    try:
        docs = vectorstore.similarity_search(question, k=k)
        context = "\n\n".join([doc.page_content for doc in docs])
        return context
    except Exception as e:
        print(f"SEARCH ERROR: {str(e)}")
        return ""