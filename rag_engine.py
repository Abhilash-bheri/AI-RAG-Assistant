import os
import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI


class Rag:
    def _init_(self):
        self.retriver=None

    def ingestion(self,data,type):
        if type=="pdf":
            loader=PyPDFLoader(data)
        if type=="web":
            loader=WebBaseLoader(f"{data}")
        documents=loader.load()
        chunks_model=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
        chunks=chunks_model.split_documents(documents)
        embs_model=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        embeddings=embs_model.embed_documents([chunk.page_content for chunk in chunks])
        vectore_store=FAISS.from_documents(documents=chunks,embedding=embs_model)
        self.retriver=vectore_store.as_retriever()
        return True
    
    def retrive(self,query):
        docs=self.retriver.invoke(query)
        return self.llm(query,"\n\n".join(doc.page_content for doc in docs))

    def llm(self,query, context):
        gemini_api_key = st.secrets["gemini_api_key"]
        model = "gemini-2.5-flash"

        llm = ChatGoogleGenerativeAI(
            model=model,
            google_api_key=gemini_api_key,
            temperature=0.2
        )

        prompt = f"""
        Answer the question only using the provided context.
        If the answer is not in the context, say "I don't know".

        Context:
        {context}

        Question:
        {query}

        Answer:
        """

        response = llm.invoke(prompt)
        
        return response.content