
# Tea Business Automation 🍵

A multi-agent AI system for automating tea business operations using FastAPI, LLMs, and RAG (Retrieval-Augmented Generation).

---

## 🚀 Overview

This project is an intelligent multi-agent system designed to automate tea business operations. It leverages LangChain agents, RAG-based product information retrieval, and LLMs to provide accurate responses about tea products, inventory, and business queries.

---

## 🧠 Key Features

- 🤖 Multi-agent architecture for complex task handling
- 📚 RAG-based product information retrieval
- 🔍 Vector search for semantic product matching
- 🍵 Tea product database integration
- ⚡ FastAPI REST endpoints for easy integration
- 🧾 Structured schema validation
- 📊 CSV-based product data management

---

## 🛠️ Tech Stack

- **Python** - Core language
- **FastAPI** - REST API framework
- **LangChain** - Agent and LLM orchestration
- **LLMs** - Language model integration
- **Vector Search** - Semantic search for products
- **Pydantic** - Data validation with schemas

---

## 📂 Project Structure

```
Tea_Business_Automation/
│
├── main.py                 # FastAPI application entry point
├── requirements.txt        # Project dependencies
├── README.md              # Project documentation
│
├── data/
│   └── products.csv       # Tea product database
│
├── endpoints/
│   └── endpoint.py        # API route handlers
│
├── schemas/
│   └── schema.py          # Pydantic data models
│
├── services/
│   ├── agents.py          # LangChain agent definitions
│   ├── config.py          # Configuration settings
│   ├── graph.py           # Agent graph/workflow builder
│   ├── model.py           # LLM model configuration
│   └── tools.py           # Custom tools for agents
│
└── rag/
    └── rag_products.py    # RAG pipeline for products
```

---

## 🔄 How It Works

1. User sends a query via the `/multi-agents` API endpoint
2. Query is processed by the multi-agent system
3. Agents retrieve relevant product information using RAG
4. LLM generates a contextual response based on retrieved data
5. Response is returned to the user

---

## 💻 Installation & Setup

### 1️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure environment

Update `services/config.py` with your LLM API keys and settings.

### 4️⃣ Run the application

```bash
python main.py
```

The API will be available at `http://0.0.0.0:8000`

---

## 📡 API Endpoints

### POST `/multi-agents`

Send queries to the multi-agent system.

**Request:**
```json
{
  "query": "What tea products do you have available?"
}
```

**Response:**
```json
{
  "answer": "We have a variety of tea products including..."
}
```

---

## 🗂️ Data Format

### Products CSV (`data/products.csv`)

The product database contains tea product information including:
- Product name
- Description
- Price
- Availability
- Category

---

## 🎯 Usage Example

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

response = client.post("/multi-agents", json={"query": "Show me available green teas"})
print(response.json())
```

---

## 📊 Possible Improvements

- Add authentication and user management
- Implement database instead of CSV
- Add caching for faster responses
- Build web UI (Streamlit/React)
- Add order processing capabilities
- Implement analytics and reporting

---

## 🧪 Future Enhancements

- Real-time inventory management
- Customer recommendation system
- Multi-language support
- Advanced search filters
- Payment integration

---

## 📝 License

This project is part of the AI Agent Course from Ostad.

---

## 👤 Author

Developed as an AI Agent automation course project.
- ✔ You think like an engineer  

👉 This is what gets interviews.

---

# 🚀 OPTIONAL (VERY STRONG BOOST)

If you want to go next level, add:

### Screenshot / Demo
```

```

### Architecture Image
(I can generate one for you if you want)

---

# 🎯 Final advice

Your repo + this README =  
👉 **Top-tier student project**

---

If you want next, I can:
- Create **architecture diagram image**
- Help you explain this in interview
- Improve your **main.py structure**

Just tell me 👍
```
