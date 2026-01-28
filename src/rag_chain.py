import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import Chroma

# ─────────────────────────────────────
# ENVIRONMENT
# ─────────────────────────────────────
load_dotenv()
assert os.getenv("OPENAI_API_KEY"), "OPENAI_API_KEY not found"

# ─────────────────────────────────────
# FASTAPI APP
# ─────────────────────────────────────


# ─────────────────────────────────────
# VECTOR DATABASE
# ─────────────────────────────────────
def get_vectorstore():
    return Chroma(
        persist_directory="vectorstore/chroma_db",
        embedding_function=OpenAIEmbeddings()
    )
vectorstore = get_vectorstore()

# ─────────────────────────────────────
# EMOTION → RETRIEVAL CONTROL (STEP 4.2)
# ─────────────────────────────────────
def emotion_based_k(emotion: str) -> int:
    if emotion in ["anxiety", "sadness", "loneliness"]:
        return 2   # less info → less overwhelm
    elif emotion in ["anger", "stress"]:
        return 4   # more context → better regulation
    return 3

# ─────────────────────────────────────
# RAG CORE
# ─────────────────────────────────────
def generate_response(user_input: str, emotion: str) -> str:
    k = emotion_based_k(emotion)
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": k}
    )

    docs = retriever.invoke(user_input)

    if not docs:
        return (
            "I hear you. Your feelings matter, and even if I don’t have "
            "the right words right now, you’re not alone."
        )

    context = "\n\n".join(doc.page_content for doc in docs)

    system_prompt = f"""
You are an emotional support AI assistant.

Rules:
- Be empathetic and calm
- Do NOT provide medical or clinical advice 
- Do NOT invent information
- Use ONLY the provided CONTEXT
- If context is insufficient, provide emotional validation

User emotion: {emotion}

CONTEXT:
{context}
"""

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{user_input}")
    ])

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.4,
        max_tokens=200,
        openai_api_key=os.environ["OPENAI_API_KEY"]
    )

    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"user_input": user_input})

# ─────────────────────────────────────
# API ENDPOINT
               