from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.schemas import ChatRequest, ChatResponse
from src.emotion_detector import detect_emotion
from src.rag_chain import generate_response

app = FastAPI(
    title="RAG-Powered Emotional Support AI",
    description="Emotion-aware AI assistant using Retrieval-Augmented Generation",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    emotion = detect_emotion(req.message)
    reply = generate_response(req.message, emotion)

    return ChatResponse(
        emotion=emotion,
        response=reply,
        explanation={"source": "rag"}
    )
