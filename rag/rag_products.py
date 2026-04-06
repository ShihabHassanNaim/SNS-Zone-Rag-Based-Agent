import pandas as pd
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load data
def load_products():
    return pd.read_csv("data/products.csv")

# Convert to documents
def create_documents(df):
    docs = []
    for _, row in df.iterrows():
        text = f"""
        Product: {row['name']}
        Category: {row['category']}
        Quality: {row['quality']}
        Buying Price: {row['buying_price']}
        Selling Price: {row['selling_price']}
        """
        docs.append(Document(page_content=text))
    return docs

# Create vector DB
def create_db(docs):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return FAISS.from_documents(docs, embeddings)