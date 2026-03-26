import os
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader

def load_documents(base_dir):
    documents = []

    for root, _, files in os.walk(base_dir):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                course = os.path.basename(os.path.dirname(file_path))

                if file.endswith(".pdf"):
                    loader = PyMuPDFLoader(file_path)
                elif file.endswith((".py", ".txt", ".md", ".cpp", ".c", ".java")):
                    loader = TextLoader(file_path)
                else:
                    continue

                doc = loader.load()

                for d in doc:
                    d.metadata["source"] = file_path
                    d.metadata["course"] = course

                documents.extend(doc)

            except Exception as e:
                print(f"Error loading {file_path}: {e}")

    return documents