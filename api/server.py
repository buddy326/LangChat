# rag_model/api/server.py

from fastapi import FastAPI
from pydantic import BaseModel

from rag_model.llm.llm import get_llm, get_embeddings
from rag_model.llm.config import BASE_DIR, CHROMA_DIR, COLLECTION_NAME

from rag_model.ingestion.loader import load_documents
from rag_model.ingestion.cleaner import clean_documents
from rag_model.ingestion.splitter import split_documents

from rag_model.vectorstore.chroma_db import get_vectorstore, initialize_vectorstore
from rag_model.rag.retriever import get_retriever
from rag_model.rag.prompt import get_prompt

import os

app = FastAPI()

llm = get_llm()
embeddings = get_embeddings()

documents = load_documents(BASE_DIR)
print(documents)
documents = clean_documents(documents)
doc_chunks = split_documents(documents)

vectorstore = get_vectorstore(embeddings, CHROMA_DIR, COLLECTION_NAME)
initialize_vectorstore(vectorstore, doc_chunks)

retriever = get_retriever(vectorstore)
prompt = get_prompt()

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
def query_rag(req: QueryRequest):
    query = req.question

    docs = retriever.invoke(query)
    context = "\n\n".join(d.page_content for d in docs)

    # generate full response (no streaming yet)
    response = llm.invoke(
        prompt.format(context=context, question=query)
    )

    # format sources
    seen = set()
    sources = []

    for d in docs:
        course = d.metadata.get("course", "Unknown Course")
        file = os.path.basename(d.metadata["source"])
        page = d.metadata.get("page", "N/A")

        key = f"{course}:{file}:{page}"

        if key not in seen:
            sources.append({
                "course": course,
                "file": file,
                "page": page
            })
            seen.add(key)

    return {
        "answer": response.content,
        "sources": sources
    }