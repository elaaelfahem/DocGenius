import os 
import streamlit as st
from dotenv import load_dotenv 
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
# --- IMPORT THE COMPONENT ---
from streamlit_chat import message 

def main(): 
    load_dotenv() 
    google_api_key = os.getenv("GOOGLE_API_KEY")
    
    st.set_page_config(page_title="ASK DocGenuis", layout="wide")
    st.header("ASK DocGenuis 📄")

    # --- INITIALIZE CHAT HISTORY ---
    if "messages" not in st.session_state:
        st.session_state.messages = [] # Format: {"role": "user/bot", "content": "text"}

    with st.sidebar:
        st.title("Settings")
        pdf = st.file_uploader("Upload your PDF", type="pdf")
    
    if pdf is not None: 
        # Logic for processing PDF (only run once using session_state)
        if "knowledge_base" not in st.session_state:
            pdf_reader = PdfReader(pdf) 
            text = "".join([page.extract_text() for page in pdf_reader.pages])
            text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200)
            chunks = text_splitter.split_text(text)
            embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
            st.session_state.knowledge_base = FAISS.from_texts(chunks, embeddings)
            st.success("Document analyzed!")

        # Chat Input
        user_question = st.text_input("Ask a question about your document:", key="user_input")
        
        if user_question: 
            # 1. Retrieve context
            docs = st.session_state.knowledge_base.similarity_search(user_question)
            
            # 2. Setup LLM
            llm = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash", 
                google_api_key=google_api_key, 
                temperature=0,
                convert_system_message_to_human=True
            )
            
            # 3. Process Answer
            chain = load_qa_chain(llm, chain_type="stuff")
            with st.spinner("DocGenuis is typing..."):
                response = chain.invoke({"input_documents": docs, "question": user_question})
                answer = response["output_text"]
                
                # Update history
                st.session_state.messages.append({"role": "user", "content": user_question})
                st.session_state.messages.append({"role": "bot", "content": answer})

    # --- DISPLAY CHAT BUBBLES ---
    for i, msg in enumerate(st.session_state.messages):
        if msg["role"] == "user":
            message(msg["content"], is_user=True, key=f"{i}_user", avatar_style="adventurer")
        else:
            message(msg["content"], key=f"{i}_bot", avatar_style="bottts")

if __name__=="__main__": 
    main()