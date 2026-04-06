from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
from .tools import web_search 
from .model import llm
from rag.rag_products import load_products, create_documents, create_db
from .model import llm




# Build once (IMPORTANT)
df = load_products()
docs = create_documents(df)
db = create_db(docs)

def product_agent(state):
    query = state["messages"][0].content.lower()

    # 🔥 HYBRID FILTERING
    if "cheap" in query:
        filtered_df = df[df["selling_price"] < 500]

    elif "premium" in query:
        filtered_df = df[df["selling_price"] > 800]

    elif "green" in query:
        filtered_df = df[df["category"] == "green"]

    else:
        filtered_df = df

    # Convert filtered data to text
    context = ""
    for _, row in filtered_df.iterrows():
        context += f"{row['name']} - Price: {row['selling_price']}\n"

    # If too many → fallback to vector search
    if len(filtered_df) > 5:
        results = db.similarity_search(query, k=3)
        context = "\n".join([r.page_content for r in results])

    prompt = f"""
    You are a tea selling assistant.

    Product Data:
    {context}

    Customer Question:
    {query}

    Give helpful suggestions with price.
    """

    response = llm.invoke(prompt)
    state["answer"] = response.content
    return state

def search_agent(state):
    agent = create_react_agent(llm, [web_search])
    messages = state["messages"]
    if messages and isinstance(messages[0], str):
        messages = [HumanMessage(content=messages[0])]
    result = agent.invoke({"messages": messages})
    state["answer"] = result["messages"][-1].content
    return state


def router_agent(state):
    return state

agent_docs = {
    "search_agent": search_agent.__doc__,
    "product_agent": product_agent.__doc__,}

def routing_logic(state):
    query = state["messages"][0].content.lower()

    if any(word in query for word in ["tea", "price", "buy", "cost", "cheap", "premium"]):
        return "product_agent"

    return "search_agent"
