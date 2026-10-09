<!-- Animated Header Banner -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20,30,40&height=220&section=header&text=AutoStream%20AI%20Agent&fontSize=32&animation=fadeIn&fontColor=ffffff&fontAlignY=38&desc=SaaS%20Conversational%20Assistant%20&%20Lead%20Capture&descSize=14&descAlignY=65" width="100%"/>
</p>

<!-- Live Status & Tech Badges -->
<p align="center">
  <img src="https://img.shields.io/badge/STATUS-ACTIVE%20%F0%9F%94%A5-success?style=for-the-badge&logo=none" alt="Status"/>
  <img src="https://img.shields.io/badge/PYTHON-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/RAG-LOCAL%20JSON-orange?style=for-the-badge&logo=json&logoColor=white" alt="RAG"/>
  <img src="https://img.shields.io/badge/WHATSAPP-READY-brightgreen?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp"/>
</p>

---

## 🤖 Overview
**AutoStream Conversational AI Agent** is a modular, intelligent assistant tailored for SaaS platforms. It expertly manages user inquiries through a robust combination of rule-based intent routing, local Retrieval-Augmented Generation (RAG), structured state management, and conversion-focused lead capture.

---

## 🏗️ Core Architecture & Pipeline

```mermaid
graph TD
    A[User Input] --> B[Intent Detection]
    B -->|Pricing / FAQ| C[Local JSON Knowledge Base RAG]
    B -->|High-Intent Lead| D[ConversationState Management]
    C --> E[Contextual Response]
    D -->|Details Collected| F[Tool Execution & Mock API]
