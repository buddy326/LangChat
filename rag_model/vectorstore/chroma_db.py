from langchain_chroma import Chroma

def get_vectorstore(embeddings, persist_dir, collection_name):
    return Chroma(
        collection_name=collection_name,
        persist_directory=persist_dir,
        embedding_function=embeddings
    )


def initialize_vectorstore(vectorstore, doc_chunks):
    if vectorstore._collection.count() == 0:
        print("Creating embeddings...")
        batch_size = 1000

        for i in range(0, len(doc_chunks), batch_size):
            batch = doc_chunks[i:i + batch_size]
            vectorstore.add_documents(batch)
            
        print("Done creating embeddings...")
        
    else:
        print("Using existing embeddings")