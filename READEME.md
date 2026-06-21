# 🤖 AI-RAG_Assistant - AI-Powered Document & Website Chat Assistant

 AI-RAG_Assistant is a Retrieval-Augmented Generation (RAG) application that allows users to chat with PDFs and websites using AI. The system retrieves relevant information from uploaded documents or web pages and generates context-aware responses using Google's Gemini model.

---

## 🚀 Features

* 📄 Chat with PDF documents
* 🌐 Chat with website content
* 🔍 Semantic search using FAISS vector database
* 🧠 AI-powered responses using Gemini
* ✂️ Automatic document chunking
* 📚 Hugging Face Embeddings
* 🎨 Interactive Streamlit UI
* ⚡ Fast retrieval and response generation

---

## 🏗️ Architecture

User Query
⬇
Retriever (FAISS)
⬇
Relevant Document Chunks
⬇
Gemini LLM
⬇
Generated Answer

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python
* LangChain

### Embeddings

* Hugging Face Embeddings
* sentence-transformers/all-mpnet-base-v2

### Vector Database

* FAISS

### LLM

* Google Gemini

### Document Loaders

* WebBaseLoader
* PyPDFLoader

---

## 📂 Project Structure

```text
AI-RAG-Assistant/
│
├── app.py
├── rag_engine.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── venv/
└── __pycache__/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Abhilash-bheri/AI-RAG-Assistant.git
cd AI-RAG-Assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
gemini_api_key=YOUR_GEMINI_API_KEY
model_name=gemini-2.5-flash
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 📖 Usage

### Website Chat

1. Enter a website URL.
2. Click "Process Document".
3. Ask questions about the website content.

### PDF Chat

1. Upload a PDF document.
2. Click "Process Document".
3. Ask questions about the PDF content.

---

## Example Questions

### Website

* What is Deno?
* What are the advantages of Bun?
* How does TypeScript work?

### PDF

* Summarize this document.
* What are the key concepts?
* Explain the main topic in simple terms.

---

## 🔮 Future Improvements

* Multi-PDF support
* Chat history
* Conversation memory
* Source citations
* Image understanding
* OCR support for scanned PDFs
* Multimodal RAG
* Cloud deployment
* Authentication system

---

## 🎯 Learning Outcomes

Through this project, I learned:

* Retrieval-Augmented Generation (RAG)
* LangChain fundamentals
* Vector databases with FAISS
* Embedding models
* Prompt engineering
* Gemini API integration
* Streamlit application development
* AI application deployment workflows

---

## 📜 License

This project is open source and available under the MIT License.

---

## 👨‍💻 Author

**Bheri Abhilash**

Aspiring AI Engineer | Python Developer | Building Intelligent Applications with Generative AI
