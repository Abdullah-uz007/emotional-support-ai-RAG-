import os
import json
from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# Load environment variables
load_dotenv()

# Load emotional knowledge
BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "emotional_knowledge.json")
with open(DATA_PATH, "r") as f:
    data = json.load(f)

# Convert JSON to Documents
documents = [] 
for item in data:
    documents.append(
        Document(
            page_content=item["content"],
            metadata={
                "emotion": item["emotion"],
                "category": item["category"],
                "source": item["source"]
            }
        )#####################################
    )

# Create embeddings
embeddings = OpenAIEmbeddings()

# Create vector database
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory="vectorstore/chroma_db"
)######################################

vectorstore.persist()

print("✅ STEP 3 COMPLETE: Vector database created successfully")
