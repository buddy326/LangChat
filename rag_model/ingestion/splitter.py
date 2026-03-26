from langchain_text_splitters import RecursiveCharacterTextSplitter

def get_splitter():
    return RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50,
        separators=["\n\n", "\n", "•", ". ", " ", ""]
    )

def split_documents(documents):
    splitter = get_splitter()
    return splitter.split_documents(documents)