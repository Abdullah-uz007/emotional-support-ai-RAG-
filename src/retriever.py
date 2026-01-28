# # src/retriever.py

# from dotenv import load_dotenv
# import os

# load_dotenv()
# assert os.getenv("OPENAI_API_KEY"), "OPENAI_API_KEY not found"

# from langchain_openai import OpenAIEmbeddings
# from langchain_community.vectorstores import Chroma

# PERSIST_DIR = "vectorstore/chroma_db"

# def get_relevant_docs(query: str, emotion: str, k: int = 3):
#     """
#     Retrieves emotionally relevant documents from vector DB.
#     """

#     embeddings = OpenAIEmbeddings()

#     vectorstore = Chroma(
#         persist_directory=PERSIST_DIR,
#         embedding_function=embeddings
#     )

#     docs = vectorstore.similarity_search(
#         query=query,
#         k=k,
#         filter={"emotion": emotion}
#     )

#     return docs
