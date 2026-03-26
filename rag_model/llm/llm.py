from langchain_ollama import ChatOllama, OllamaEmbeddings

def get_llm():
    return ChatOllama(model="phi3")

def get_embeddings():
    return OllamaEmbeddings(model="nomic-embed-text")