import streamlit as st
from rag_engine import Rag

st.set_page_config(
    page_title="AI RAG Assistant",
    page_icon="🤖",
    layout="wide"
)
if "rag" not in st.session_state:
    st.session_state.rag = Rag()

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

st.info("Provide either a Website URL or a PDF document")

submit = st.button(
    "🚀 Process Document",
    use_container_width=True
)

if submit:

    if not url and not pdf:
        st.error(
            "Please provide a URL or upload a PDF"
        )

    elif url:
        with st.spinner("Processing Url..."):
            if obj.ingestion(url,type="web"):
                data="Website processed successfully!"
            else:
                data="there is an issue"
            with st.spinner(
                "Processing Website..."
            ):
                st.success(data)

    elif pdf:

        with st.spinner("Processing PDF..."):

            with open("uploaded.pdf", "wb") as f:
                f.write(pdf.getbuffer())

            obj.ingestion("uploaded.pdf", "pdf")

            st.success("PDF Loaded")
st.divider()

st.subheader("💬 Ask Questions")

question = st.chat_input(
    "Ask anything about the uploaded content..."
)

if question:

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = obj.retrive(question)
            st.write(answer)



