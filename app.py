import os 
import streamlit as st
from dotenv import load_dotenv 
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain

def main(): 
    load_dotenv() 
    google_api_key = os.getenv("GOOGLE_API_KEY")
    
    st.set_page_config(page_title="ASK DocGenuis")
    st.header("ASK DocGenuis 📄")

    pdf = st.file_uploader("Upload your PDF", type="pdf")
    
    if pdf is not None: 
        pdf_reader = PdfReader(pdf) 
        text = ""
        for page in pdf_reader.pages: 
            text += page.extract_text()

        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text)

        # Local embeddings (Free & No API key needed)
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        knowledge_base = FAISS.from_texts(chunks, embeddings)

        user_question = st.text_input("Ask a question about your document:")
        
        if user_question: 
            docs = knowledge_base.similarity_search(user_question)
            
            # 2. Initialize Gemini
            llm = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash", 
                google_api_key=google_api_key, 
                temperature=0,
                convert_system_message_to_human=True
            )
            
            # 3. Use load_qa_chain and .invoke()
            chain = load_qa_chain(llm, chain_type="stuff")
            
            with st.spinner("Analyzing document..."):
                # Use .invoke() instead of .run()
                response = chain.invoke({"input_documents": docs, "question": user_question})
                
                st.subheader("Answer:")
                # Use the correct key to pull the text out
                st.write(response["output_text"])
 
if __name__=="__main__": 
    main()