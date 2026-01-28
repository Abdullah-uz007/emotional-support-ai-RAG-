
<p align="center">
  <img src="assets/banner.png" alt="RAG-Powered AI Health Assistant" width="100%" />
</p>

# 🧠 RAG-Powered AI Health Assistant

Your personal AI companion for emotional and health insights, powered by **Retrieval-Augmented Generation (RAG)**.

This project combines **LLMs, vector databases, and emotion detection** to deliver context-aware, empathetic responses based on trusted knowledge sources.

---

## ✨ Features

- 🧠 **Emotion Detection** from user input  
- 📚 **RAG Pipeline** for grounded, factual responses  
- 🔍 **Vector Search** using embeddings  
- 💬 **Empathetic AI Responses**  
- 🖥️ **Streamlit Frontend**  
- ⚡ **FastAPI Backend (modular design)**  
- 🐳 **Docker-ready**

---

## 🗂️ Project Structure

```

emotional-rag-ai/
│
├── assets/
│   └── banner.png
│
├── data/
│   └── emotional_knowledge.json
│
├── frontend/
│   └── app.py
│
├── src/
│   ├── emotion_detector.py
│   ├── ingest.py
│   ├── rag_chain.py
│   ├── retriever.py
│   ├── schemas.py
│   └── app.py
│
├── tests/
│   ├── test_emotion.py
│   ├── test_rag.py
│   └── test_retriever.py
│
├── .gitignore
├── .dockerignore
├── Dockerfile
├── requirements.txt
└── README.md

````

---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Abdullah-uz007/emotional-support-ai-RAG-.git
cd emotional-rag-ai
````

---

### 2️⃣ Create & activate virtual environment

```bash
python -m venv venv311
source venv311/Scripts/activate   # Windows (Git Bash)
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set environment variables

Create a `.env` file in the root:

```env
OPENAI_API_KEY=your_api_key_here
```

⚠️ **Never commit `.env` files**

---

## 🧪 Ingest Knowledge Base

```bash
python src/ingest.py
```

This creates embeddings and stores them in the vector database.

---

## 🖥️ Run the Backend (API)

```bash
uvicorn src.app:app --reload
```

---

## 🎨 Run the Frontend (Streamlit)

```bash
cd frontend
streamlit run app.py
```

Open browser at:
👉 [http://localhost:8501](http://localhost:8501)

---

## 🐳 Docker (Optional)

```bash
docker build -t emotional-rag-ai .
docker run -p 8000:8000 -p 8501:8501 emotional-rag-ai
```

---

## 🧠 How It Works

1. User enters text
2. Emotion is detected
3. Relevant documents are retrieved from vector DB
4. LLM generates a **grounded & empathetic response**

---

## ⚠️ Disclaimer

This project is for **educational and research purposes only**.
It is **not a substitute for professional medical or mental health advice**.

---

## 🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first.

---
