from src.emotion_detector import detect_emotion
from src.rag_chain import generate_response

user_input = "I feel really anxious and can't focus"

emotion = detect_emotion(user_input)
response = generate_response(user_input, emotion)

print("Emotion:", emotion)
print("Response:\n", response)
