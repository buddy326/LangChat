from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader
import re


load_dotenv()

llm = ChatOllama(model="phi3")
output_parser = StrOutputParser()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chain = llm | output_parser

BASE_DIR = "UvicClasses"

documents = []

for root, dirs, files in os.walk(BASE_DIR):
    for file in files:
        file_path = os.path.join(root, file)

        try:
            if file.endswith(".pdf"):
                loader = PyMuPDFLoader(file_path)
                doc = loader.load()
                for d in doc:
                    d.metadata["source"] = file_path
                documents.extend(doc)

            elif file.endswith((".py", ".txt", ".md", ".cpp", ".c", ".java")):
                loader = TextLoader(file_path)
                doc = loader.load()
                for d in doc:
                    d.metadata["source"] = file_path
                documents.extend(doc)

        except Exception as e:
            print(f"Error loading {file_path}: {e}")

print(f"Loaded {len(documents)} documents")

def clean_text(text):
    text = re.sub(r"University of Victoria.*\n", "", text)
    text = re.sub(r"Department of Computer Science\n", "", text)
    text = re.sub(r"CSC 230: Computer Architecture and Assembly Language\n", "", text)
    text = re.sub(r"Images?:.*", "", text)  # remove image lines
    text = re.sub(r"http\S+", "", text)    # remove URLs
    return text


for d in documents:
    d.page_content = clean_text(d.page_content)
    
for d in documents[:5]:
    print("----")
    print(d.page_content)