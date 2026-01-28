from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
import os

load_dotenv()

assert os.getenv("OPENAI_API_KEY"), "OPENAI_API_KEY not found"


# Allowed emotions (controlled vocabulary)
EMOTIONS = ["anxiety", "sadness", "stress", "anger", "loneliness", "neutral"]

def detect_emotion(user_input: str) -> str:
    """
    Classifies user emotion into a controlled label.
    """

    prompt = ChatPromptTemplate.from_messages([
        ("system",
         "You are an emotion classification system. "
         "Classify the user's emotional state into ONE of these labels only:\n"
         "anxiety, sadness, stress, anger, loneliness, neutral.\n"
         "Respond with ONLY the label, no explanation."
        ),
        ("human", "{text}")
    ])

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    chain = prompt | llm | StrOutputParser()
    emotion = chain.invoke({"text": user_input}).strip().lower()

    # Safety fallback
    if emotion not in EMOTIONS:
        return "neutral"

    return emotion
