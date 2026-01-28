from src.emotion_detector import detect_emotion


tests = [
    "I feel nervous and my chest feels tight",
    "I feel so alone lately",
    "Everything is making me angry",
    "I just feel empty today",
    "I am fine"
]

for t in tests:
    print(t, "→", detect_emotion(t))
