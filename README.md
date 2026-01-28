## ▶️ Run the Project

### 1. Backend
```bash
uvicorn src.app:app --reload



frontend
streamlit run frontend/app.py


ngest Knowledge (one-time)
python src/ingest.py





This helps **reviewers instantly run it**.

---

## 🔧 STEP 5: Explain Code Logic (For Viva / Video)

### 🧠 30-second explanation (memorize this):

> “The system first detects the user’s emotion using a language model constrained to fixed labels.  
Based on that emotion, the retriever dynamically adjusts how many documents it fetches from a local vector database.  
Only emotionally relevant context is retrieved, and the LLM is instructed to respond empathetically using *only that context*, preventing hallucinations.”

🔥 This sounds **senior-level**, not student-level.

---

## 🔧 STEP 6: Final Git Commands (Now from ROOT)

From:
