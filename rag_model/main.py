from dotenv import load_dotenv

from rag_model.llm.config import BASE_DIR, CHROMA_DIR, COLLECTION_NAME
from rag_model.llm.llm import get_llm, get_embeddings

from rag_model.ingestion.loader import load_documents
from rag_model.ingestion.cleaner import clean_documents
from rag_model.ingestion.splitter import split_documents

from rag_model.vectorstore.chroma_db import get_vectorstore, initialize_vectorstore

from rag_model.rag.retriever import get_retriever
from rag_model.rag.prompt import get_prompt
from rag_model.rag.pipeline import run_query

load_dotenv()

# setup
llm = get_llm()
embeddings = get_embeddings()

# ingestion
documents = load_documents(BASE_DIR)
documents = clean_documents(documents)
doc_chunks = split_documents(documents)

# vectorstore
vectorstore = get_vectorstore(embeddings, CHROMA_DIR, COLLECTION_NAME)
initialize_vectorstore(vectorstore, doc_chunks)

# rag
retriever = get_retriever(vectorstore)
prompt = get_prompt()

# run
run_query(llm, retriever, prompt, "What is cache memory?")