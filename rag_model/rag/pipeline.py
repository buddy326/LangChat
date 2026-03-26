import os

def run_query(llm, retriever, prompt, query):
    docs = retriever.invoke(query)

    context = "\n\n".join(d.page_content for d in docs)

    print("\nANSWER:\n")

    for chunk in llm.stream(
        prompt.format(context=context, question=query)
    ):
        print(chunk.content, end="", flush=True)

    print("\n\nSOURCES:\n")

    seen = set()

    for i, d in enumerate(docs, 1):
        course = d.metadata.get("course", "Unknown Course")
        file = os.path.basename(d.metadata["source"])
        page = d.metadata.get("page", "N/A")

        key = f"{course}:{file}:{page}"

        if key not in seen:
            print(f"[{i}] {course} / {file} (page {page})")
            seen.add(key)