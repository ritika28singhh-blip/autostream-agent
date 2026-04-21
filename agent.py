import json

def load_knowledge():
    with open("knowledge_base.json") as f:
        return json.load(f)

def retrieve_answer(query, kb):
    query = query.lower()

    if "price" in query or "plan" in query:
        return f"""
📦 Pricing:

Basic Plan: {kb['pricing']['basic']['price']} - {', '.join(kb['pricing']['basic']['features'])}

Pro Plan: {kb['pricing']['pro']['price']} - {', '.join(kb['pricing']['pro']['features'])}
"""
    elif "refund" in query:
        return kb["policies"]["refund"]
    elif "support" in query:
        return kb["policies"]["support"]

    return "Sorry, I couldn't find that info."
