# AutoStream Conversational AI Agent

##  How to Run

```bash
git clone <your-repo-link>
cd autostream-agent
pip install -r requirements.txt
python app.py
```

---

##  Architecture Explanation

This project implements a conversational AI agent for a SaaS product called AutoStream. The system is designed using a modular architecture that includes intent detection, retrieval-augmented generation (RAG), and tool execution.

Intent detection is handled using a rule-based approach that classifies user input into greeting, pricing inquiries, or high-intent leads. This ensures quick and predictable responses.

The RAG pipeline uses a local JSON knowledge base containing pricing details and company policies. This allows the agent to retrieve accurate and controlled information without relying on external APIs.

State management is implemented using a custom ConversationState class, which stores user data such as name, email, and platform across multiple conversation turns.

The agent includes a tool execution mechanism where a mock API is triggered only after collecting all required user details, ensuring proper lead capture flow.

---

##  WhatsApp Integration (Concept)

To integrate this agent with WhatsApp:

1. Use WhatsApp Business API (via Meta or Twilio)
2. Create a webhook using Flask or FastAPI
3. Receive user messages via webhook
4. Pass message to chatbot()
5. Send response back through WhatsApp API

Flow:
User → WhatsApp → Webhook → Agent → Response → WhatsApp

---

##  Demo

This project demonstrates:

* Pricing query handling
* Intent detection
* Lead capture flow
* Tool execution
