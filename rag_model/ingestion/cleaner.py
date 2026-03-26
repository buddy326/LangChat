import re

def clean_text(text):
    text = re.sub(r"University of Victoria.*\n", "", text)
    text = re.sub(r"Department of Computer Science\n", "", text)
    text = re.sub(r"CSC 230: Computer Architecture and Assembly Language\n", "", text)
    text = re.sub(r"Images?:.*", "", text)
    text = re.sub(r"http\S+", "", text)
    return text


def clean_documents(documents):
    for d in documents:
        d.page_content = clean_text(d.page_content)
    return documents