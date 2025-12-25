# 📄 Ask DocGenius  
**AI-Powered PDF Question Answering System**

Ask DocGenius is a web-based application that allows users to upload PDF documents and ask natural language questions about their content. The system combines semantic search, vector databases, and Google Gemini to generate accurate, context-aware answers grounded in the document.

---

## ✨ Features

- Upload and analyze PDF documents
- Semantic text chunking and embedding
- Fast similarity search using FAISS
- AI-powered question answering with Google Gemini
- Clean and interactive Streamlit interface
- Local embedding generation for improved privacy

---

## 🏗️ Architecture

1. PDF text extraction using PyPDF2  
2. Text chunking with overlap for better context retention  
3. Embedding generation using HuggingFace MiniLM  
4. Vector storage and retrieval with FAISS  
5. Context-aware answer generation using Google Gemini via LangChain  

---

## 🧰 Technology Stack

| Component | Technology |
|---------|-----------|
| Frontend | Streamlit |
| LLM | Google Gemini (`gemini-2.5-flash`) |
| Embeddings | HuggingFace (`all-MiniLM-L6-v2`) |
| Vector Database | FAISS |
| Framework | LangChain |
| PDF Parsing | PyPDF2 |
| Environment | Python, dotenv |

---



## 🔑 Requirements

- Python 3.9+
- Google Gemini API key


### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ask-docgenius.git
cd ask-docgenius

