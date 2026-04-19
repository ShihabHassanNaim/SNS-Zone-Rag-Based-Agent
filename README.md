
# Tea Business Automation System

> An intelligent multi-agent AI system for automating tea business operations using FastAPI, LangChain, and Retrieval-Augmented Generation (RAG).

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-green)
![LangChain](https://img.shields.io/badge/LangChain-latest-red)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## Overview

This project implements an enterprise-grade multi-agent system designed to automate tea business operations. The system leverages advanced AI techniques including LangChain for agent orchestration, RAG for intelligent product information retrieval, and LLMs for natural language understanding and generation.

### Key Benefits

- **Intelligent Query Processing**: Multi-agent architecture handles complex business queries
- **Context-Aware Responses**: RAG ensures responses are grounded in actual product data
- **Scalable API**: FastAPI provides high-performance REST endpoints
- **Easy Integration**: Clean, well-documented API for seamless third-party integration

---

## Features

- **Multi-Agent Architecture**: Orchestrated agents handle specialized business tasks
- **RAG Pipeline**: Semantic search retrieves relevant product information
- **Vector Search**: Fast similarity matching for product queries
- **RESTful API**: FastAPI endpoints for easy integration
- **Data Validation**: Pydantic schemas ensure data integrity
- **CSV Database**: Simple yet effective product data management

---

## Technology Stack

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.8+ |
| **API Framework** | FastAPI |
| **Agent Framework** | LangChain |
| **LLM Integration** | LLM API (OpenAI/Claude/Local) |
| **Data Validation** | Pydantic |
| **Search** | Vector/Semantic Search |
| **Server** | Uvicorn |

---

## Project Structure

```
Tea_Business_Automation/
│
├── main.py                      # Application entry point
├── requirements.txt             # Python dependencies
├── README.md                    # Documentation
│
├── data/
│   └── products.csv             # Tea product database
│
├── endpoints/
│   └── endpoint.py              # API route handlers
│
├── schemas/
│   └── schema.py                # Pydantic data models
│
├── services/
│   ├── agents.py                # Agent definitions
│   ├── config.py                # Configuration management
│   ├── graph.py                 # Workflow orchestration
│   ├── model.py                 # LLM configuration
│   └── tools.py                 # Custom agent tools
│
└── rag/
    └── rag_products.py          # RAG pipeline implementation
```

---

## Prerequisites

Before getting started, ensure you have:

- **Python 3.8 or higher** installed
- **pip** package manager
- **Virtual environment tool** (recommended)
- **LLM API Keys** (OpenAI, Claude, or local LLM setup)

---

## Installation

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd Tea_Business_Automation
```

### Step 2: Create Virtual Environment

```bash
# Linux/macOS
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment

Update `services/config.py` with your configuration:

```python
# LLM API Key
LLM_API_KEY = "your-api-key-here"

# Model Settings
MODEL_NAME = "gpt-4"  # or your preferred model
```

### Step 5: Run the Application

```bash
python main.py
```

The API will be available at: `http://localhost:8000`

### View API Documentation

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

---

## API Documentation

### Endpoint: `/multi-agents`

Send natural language queries to the multi-agent system.

**Method**: `POST`

**Request Body**:
```json
{
  "query": "What are the available green tea products?"
}
```

**Response**:
```json
{
  "answer": "We have a selection of premium green teas including Dragon Well, Sencha, and Matcha. Each offers unique flavor profiles..."
}
```

**Status Codes**:
- `200`: Success
- `400`: Invalid request
- `500`: Server error

---

## System Architecture

```
┌─────────────────────────────────────┐
│      User Query (FastAPI)           │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│   Query Processing & Validation     │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│     Multi-Agent Orchestration       │
│   (LangChain Graph Execution)       │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│   RAG Pipeline & Vector Search      │
│  (Retrieve Product Information)     │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│    LLM Processing & Generation      │
│   (Context-Aware Response)          │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│      Return Response to User        │
└─────────────────────────────────────┘
```

---

## Data Format

### Products Database (`data/products.csv`)

The product database should contain the following fields:

```csv
id,name,description,price,category,availability,quantity
1,Green Tea Sencha,Premium Japanese green tea,12.99,Green Tea,In Stock,50
2,Oolong Tea,Authentic Chinese oolong,15.99,Oolong,In Stock,35
3,Black Tea Assam,Strong Indian black tea,11.99,Black Tea,In Stock,40
```

---

## Usage Example

### Python Client

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Query the system
response = client.post(
    "/multi-agents",
    json={"query": "Show me premium green teas under $15"}
)

# Process response
result = response.json()
print(f"Answer: {result['answer']}")
```

### cURL

```bash
curl -X POST "http://localhost:8000/multi-agents" \
  -H "Content-Type: application/json" \
  -d '{"query": "What green teas do you have?"}'
```

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Port 8000 already in use | Change port in `main.py` or kill existing process |
| Missing dependencies | Run `pip install -r requirements.txt` |
| LLM API key errors | Verify API key in `services/config.py` |
| CSV file not found | Ensure `data/products.csv` exists |

### Debugging

Enable verbose logging in `services/config.py`:

```python
LOG_LEVEL = "DEBUG"
```

---

## Roadmap

### Short Term
- [ ] Add authentication and user management
- [ ] Implement database layer (PostgreSQL/MongoDB)
- [ ] Add request caching

### Medium Term
- [ ] Build web dashboard (React/Vue)
- [ ] Implement order processing
- [ ] Add analytics dashboard

### Long Term
- [ ] Real-time inventory synchronization
- [ ] Multi-language support
- [ ] Advanced recommendation system
- [ ] Payment gateway integration

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add improvement'`)
4. Push to branch (`git push origin feature/improvement`)
5. Create a Pull Request

---

## License

This project is part of the **AI Agent Course** from **Ostad**.

---

## Support & Contact

For questions, issues, or suggestions, please open an issue in the repository.

---

**Last Updated**: April 2026  
**Version**: 1.0.0
