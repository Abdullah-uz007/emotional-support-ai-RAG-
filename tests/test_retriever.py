from retriever import get_relevant_docs

query = "I feel nervous and my heart is racing"
emotion = "anxiety"

docs = get_relevant_docs(query, emotion)

for d in docs:
    print("-" * 40)
    print(d.page_content)
    print("META:", d.metadata)
