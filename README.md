# 📚 StudyMate AI
### An Intelligent Study Assistant for University Students
> Powered by Groq LLaMA 3.3 · LangChain · RAG · Streamlit
 
![Python](https://img.shields.io/badge/Python-3.14-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Cloud-red)
![Groq](https://img.shields.io/badge/Groq-LLaMA3.3-purple)
![License](https://img.shields.io/badge/License-MIT-green)
 
---
 
## 🌐 Live Demo
👉 **[https://studymate-ai-2ynppfpwh8wurbv3yuhqvr.streamlit.app/](https://studymate-ai-2ynppfpwh8wurbv3yuhqvr.streamlit.app/)**
 
---
 
## 📌 Project Overview
 
StudyMate AI is an AI-powered web application built for university students to help them study smarter. Students can upload their lecture notes or textbook chapters in PDF format and instantly get summaries, MCQs, flashcards, and answers to their questions — all grounded in their own uploaded material.
 
This project was developed as a Capstone Project for the **Introduction to Artificial Intelligence** course at **Hamdard University (Main Campus)**.
 
| Detail | Info |
|--------|------|
| Student | Arqam Siddiqui |
| CMS ID | 2592-2024 |
| Course | Introduction to Artificial Intelligence |
| University | Hamdard University, Main Campus |
| Duration | 3 Weeks |
 
---
 
## ✨ Features
 
| Feature | Description |
|---------|-------------|
| 📝 **Auto Summary** | Generates key points and important terms from any PDF |
| ❓ **MCQ Generator** | Creates 5 multiple choice questions for self-testing |
| 💬 **Q&A Chatbot** | RAG-based chatbot that answers from your uploaded PDF |
| 🃏 **Flashcards** | Creates quick revision flashcards for key concepts |
| 🧒 **Explain Simply** | Explains difficult concepts in simple, easy language |
 
---
 
## 🤖 AI Techniques Used
 
1. **Prompt Engineering** — Custom prompts designed for Summary, MCQ, Flashcard, and Q&A tasks
2. **LLM API Integration** — Groq API with LLaMA 3.3-70B model for fast AI responses
3. **Retrieval-Augmented Generation (RAG)** — LangChain pipeline ensures answers come strictly from uploaded PDF
4. **Vector Embeddings** — HuggingFace `all-MiniLM-L6-v2` + ChromaDB for semantic document search
> ✅ Uses **4 AI techniques** — exceeds course requirement of minimum 2
 
---
 
## 🛠️ Tools & Technologies
 
| Tool | Purpose |
|------|---------|
| Python 3.14 | Programming Language |
| Streamlit | Web UI Framework |
| Groq API (LLaMA 3.3-70B) | Large Language Model |
| LangChain | RAG Pipeline |
| ChromaDB | Vector Database |
| HuggingFace Embeddings | Text Embeddings (all-MiniLM-L6-v2) |
| PyPDF | PDF Text Extraction |
| python-dotenv | Environment Variable Management |
 
---
 
## 🏗️ System Architecture
 
```
Student (User)
     ↓
Streamlit Web UI
     ↓
PDF Processor (PyPDF + LangChain)
     ↓
Vector Embeddings + ChromaDB
     ↓
RAG + Groq LLM (LLaMA 3.3-70B)
     ↓
Response → Summary / MCQ / Q&A / Flashcards
```
 
---
 
## 🚀 How to Run Locally
 
### 1. Clone the Repository
```bash
git clone https://github.com/your-username/StudyMate-AI.git
cd StudyMate-AI
```
 
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
 
### 3. Add API Key
Create a `.env` file in the root folder:
```
GROQ_API_KEY=your_groq_api_key_here
```
Get your free Groq API key at: [console.groq.com](https://console.groq.com)
 
### 4. Run the App
```bash
python -m streamlit run app.py
```
 
### 5. Open in Browser
```
http://localhost:8501
```
 
---
 
## 📁 Project Structure
 
```
StudyMate-AI/
├── app.py              # Main Streamlit application
├── rag.py              # RAG pipeline (PDF processing + ChromaDB)
├── prompts.py          # All AI prompt templates
├── requirements.txt    # Python dependencies
├── .env                # API keys (not uploaded to GitHub)
├── .gitignore          # Git ignore file
└── README.md           # Project documentation
```
 
---
 
## ⚠️ Ethical Considerations
 
| Risk | Mitigation |
|------|-----------|
| Exam cheating | Disclaimer: "For study & revision purposes only" |
| AI hallucinations | RAG ensures answers come strictly from uploaded PDF |
| Data privacy | No PDFs stored permanently — deleted after session |
| Copyright issues | Users upload only their own or educational content |
| Over-reliance on AI | App encourages verification with original notes |
 
---
 
## 🐛 Known Limitations
 
- Scanned/image-based PDFs are not supported (text PDFs only)
- Maximum PDF size: 50MB
- Internet connection required for Groq API
- Answers limited to content within the uploaded PDF
---
 
## 🔮 Future Improvements
 
- 📱 Mobile app version
- 🌐 Multi-language support (Urdu)
- 🔊 Voice Q&A feature
- 📊 Student progress tracking dashboard
- 🤝 Multi-PDF support
- 🧑‍🏫 Teacher quiz export feature
---
 
## 👨‍💻 Developer
 
**Arqam Siddiqui**
CMS ID: 2592-2024
Hamdard University, Main Campus
Introduction to Artificial Intelligence — Capstone Project
 
---
 
*StudyMate AI — Empowering Students with Artificial Intelligence* 📚
