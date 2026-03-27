import re

def clean_text(text):
    # ----------------------------
    # Remove headers / noise
    # ----------------------------
    text = re.sub(r"University of Victoria.*\n", "", text)
    text = re.sub(r"Department of Computer Science\n", "", text)
    text = re.sub(r"CSC 230: Computer Architecture and Assembly Language\n", "", text)

    # remove image lines + URLs
    text = re.sub(r"Images?:.*", "", text)
    text = re.sub(r"http\S+", "", text)

    # ----------------------------
    # Preserve code blocks
    # ----------------------------
    parts = re.split(r"(```.*?```)", text, flags=re.DOTALL)

    cleaned_parts = []

    for part in parts:
        if part.startswith("```"):
            # keep code blocks untouched
            cleaned_parts.append(part)
        else:
            # single newline → space
            part = re.sub(r"(?<!\n)\n(?!\n)", " ", part)

            # multiple newlines → max two
            part = re.sub(r"\n{2,}", "\n\n", part)

            # remove extra spaces/tabs
            part = re.sub(r"[ \t]+", " ", part)

            cleaned_parts.append(part)

    return "".join(cleaned_parts).strip()


def clean_documents(documents):
    for d in documents:
        d.page_content = clean_text(d.page_content)
    return documents