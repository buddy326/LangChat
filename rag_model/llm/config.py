import os

# get project root (LangChat/)
ROOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../")
)

BASE_DIR = os.path.join(ROOT_DIR, "UvicClasses")
CHROMA_DIR = os.path.join(ROOT_DIR, "chroma_db")
COLLECTION_NAME = "SENG_documents"