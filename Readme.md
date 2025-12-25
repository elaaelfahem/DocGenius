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

## 📁 Project Structure

├── app.py
├── .env
├── requirements.txt
└── README.md

---

## 🔑 Requirements

- Python 3.9+
- Google Gemini API key

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ask-docgenius.git
cd ask-docgenius
2. Create a Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

🔐 Environment Setup

Create a .env file in the project root:

GOOGLE_API_KEY=your_google_gemini_api_key

▶️ Usage

Run the Streamlit application:

streamlit run app.py


Open your browser at:

http://localhost:8501

🧠 Model Configuration

Embedding Model: all-MiniLM-L6-v2

Language Model: gemini-2.5-flash

Temperature: 0

QA Chain Type: stuff

🔒 Privacy Considerations

Embeddings are generated locally

Only relevant document chunks are sent to the language model

Uploaded PDFs are not stored

🚧 Limitations

Single PDF support

No persistent conversation memory

Performance depends on document size and formatting

🛣️ Future Work

Multi-document querying

Source citation in answers

Chat history and memory

Deployment with Docker or cloud services

UI/UX improvements

👩‍💻 Author

Elaa 
Engineering Student | AI & Machine Learning Enthusiast