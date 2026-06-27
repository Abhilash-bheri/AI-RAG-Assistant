import streamlit as st
from rag_engine import Rag

st.set_page_config(
    page_title="AI RAG Assistant",
    page_icon="🤖",
    layout="wide"
)

if "rag" not in st.session_state:
    st.session_state.rag = Rag()

if "messages" not in st.session_state:
    st.session_state.messages = []

obj = st.session_state.rag


st.title("🤖 AI RAG Assistant")
st.caption("Chat with PDFs and Websites using AI")

st.divider()

st.subheader("📂 Upload Knowledge Source")

col1, col2 = st.columns(2)

with col1:
    url = st.text_input(
        "🌐 Website URL",
        placeholder="https://example.com"
    )

with col2:
    pdf = st.file_uploader(
        "📄 Upload PDF",
        type=["pdf"]
    )

st.info("Provide either a Website URL or upload a PDF document.")

if st.button("🚀 Process Document", use_container_width=True):

    if not url and not pdf:
        st.error("Please provide a Website URL or upload a PDF.")

    elif url:

        with st.spinner("Processing Website..."):

            if obj.ingestion(url, "web"):
                st.success("✅ Website processed successfully!")
            else:
                st.error("❌ Failed to process website.")

    elif pdf:

        with open("uploaded.pdf", "wb") as f:
            f.write(pdf.getbuffer())

        with st.spinner("Processing PDF..."):

            if obj.ingestion("uploaded.pdf", "pdf"):
                st.success("✅ PDF processed successfully!")
            else:
                st.error("❌ Failed to process PDF.")

st.divider()


col1, col2 = st.columns([8, 1])

with col1:
    st.subheader("💬 Ask Questions")

with col2:
    if st.button("🗑️"):
        st.session_state.messages = []
        st.rerun()


for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input(
    "Ask anything about the uploaded content..."
)

if question:


    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)


    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer = obj.retrive(question)

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.rerun()