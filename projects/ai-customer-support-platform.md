<a id="top"></a>

[← Back to portfolio](../README.md)

**Language:** English | [Português](ai-customer-support-platform.pt-BR.md)

# AI Customer Support Platform 🎧

[![LangGraph](https://img.shields.io/badge/LangGraph-supervisor-1C3C3C?style=flat-square)](https://www.langchain.com/langgraph)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Next.js%2016-000000?style=flat-square&logo=nextdotjs&logoColor=white)](https://nextjs.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-pgvector-4169E1?style=flat-square&logo=postgresql&logoColor=white)](https://github.com/pgvector/pgvector)
[![Redis](https://img.shields.io/badge/Redis-pub%2Fsub-DC382D?style=flat-square&logo=redis&logoColor=white)](https://redis.io/)
[![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-Langfuse-425CC7?style=flat-square&logo=opentelemetry&logoColor=white)](https://opentelemetry.io/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)

**Repository:** [AI-Customer-Support-Platform-With-Langgraph](https://github.com/OtnielGomes/AI-Customer-Support-Platform-With-Langgraph)

<div align="center">
  <a href="https://github.com/OtnielGomes/AI-Customer-Support-Platform-With-Langgraph">
    <img src="covers/ai-customer-support-platform/cover.en.png" alt="ai-customer-support-platform cover" width="900">
  </a>
</div>

| | |
|---|---|
| **Context** | Independent portfolio |
| **Timeline** | 2025 — 2026 |
| **Focus area** | Multi-agent support, policy engine & RAG |

LangGraph · FastAPI · Next.js · PostgreSQL/pgvector · Redis · Langfuse · Docker

## Overview

A support assistant that talks about orders has to be right about them. It must answer *when will my package arrive* from the actual shipment row, refuse a refund the policy does not allow, and hand the conversation to a human when automation is not authorized. An LLM asked to do this from context alone will invent order states and approve refunds it should not.

A **LangGraph supervisor** classifies intent and delegates to billing, logistics, or account workers. Three sources of truth stay separate: **PostgreSQL** for operational facts, a **deterministic policy engine** (`company.yaml`) for money and deadlines, and **RAG over pgvector** for procedures and FAQs—operational rows are deliberately excluded from the index. Tools are scoped to the authenticated customer; the **Next.js** BFF keeps API keys off the browser.

The product ships as **Customer Portal** and **Support Console** with SSE live chat, human takeover on the same thread, guardrails for jailbreak and prompt injection, and an analytics console fed by OpenTelemetry and Langfuse. Deployed on **DigitalOcean App Platform** (API, web, Postgres/pgvector, Valkey).


## Architecture

Supervisor, domain agents, facts, policy, and knowledge—without collapsing them into the prompt.

![Architecture diagram](architecture-cases/ai-customer-support-platform-en.png)

## Implementation walkthrough

### PHASE 01 — Authentication and BFF

Email-only portal login rejects unknown customers. Next.js routes chat and ticket APIs through a backend-for-frontend so secrets never reach the client.

### PHASE 02 — Guardrails and graph entry

Incoming messages pass safety checks before the LangGraph workflow runs. Failed guardrails short-circuit to refusal or escalation paths.

### PHASE 03 — Supervisor and scoped tools

The supervisor picks billing, logistics, account, or escalation workers. Tools (`get_order`, `get_payments`, `get_shipment`, `check_refund_eligibility`) are bound to the ticket’s customer ID.

### PHASE 04 — Policy vs RAG vs database

Facts come from SQL queries. Refund and threshold rules are evaluated in Python before any destructive action. RAG retrieves policy *explanations* from `data/knowledge_base/`, not live order rows.

### PHASE 05 — Live chat, takeover, and observability

Redis pub/sub fans out SSE token streams; messages persist for human pickup mid-thread. Escalation pauses automation while agents use the Support Console with tool traces. Langfuse and OpenTelemetry back intent mix, latency, and tool error dashboards.

## Tech stack deep-dive

### LangGraph

Explicit supervisor/worker graph matches how support teams think about intents and handoffs.

### Policy engine (YAML + Python)

Numbers that cost money when wrong are not negotiable in a system prompt.

### pgvector RAG

Grounds procedural answers while keeping transactional data in SQL where it belongs.

### Redis / Valkey

Cache and pub/sub for responsive chat and multi-tab console updates.

### Langfuse + OpenTelemetry

Production-grade tracing for eval harnesses (intent, tool correctness, policy compliance).

### Docker & GitHub Actions

Reproducible synthetic world (`SCN-*` anomalies) for demos and regression evals.

## Screenshots

<details>
<summary>Customer Portal — login, orders, and live chat</summary>

Email-only login. Unknown addresses are rejected; the portal never creates customers on the fly.

<img src="../images/ai-customer-support-platform-with-langgraph/interface-portal-customer_EN.png" alt="Customer portal login" width="900">

After sign-in the portal recognizes the customer's orders and opens a live chat from the same screen.

<img src="../images/ai-customer-support-platform-with-langgraph/portal-customer-orders_EN.png" alt="Customer home with orders" width="900">

Routine questions — estimated delivery, payment status, items — are answered from PostgreSQL rows.

<img src="../images/ai-customer-support-platform-with-langgraph/order-interaction-0_EN.png" alt="Assistant answering when an order will arrive" width="900">

<img src="../images/ai-customer-support-platform-with-langgraph/order-interaction-1.png" alt="Order follow-up in the chat" width="900">

</details>

<details>
<summary>Human-in-the-loop — escalation and takeover</summary>

When automation cannot resolve the case — a payment mismatch, an identity check, a refund outside the policy window — the ticket escalates and a human continues in the same thread. The customer sees one conversation, not a handoff.

<img src="../images/ai-customer-support-platform-with-langgraph/order-interaction-3-human-intervection.png" alt="Escalation raised in the portal" width="900">

<img src="../images/ai-customer-support-platform-with-langgraph/order-interaction-4-human-intervection_EN.png" alt="Human reply inside the portal thread" width="900">

A high-value refund is not executed by the assistant. The policy engine returns the verdict, and the request goes to a person.

<img src="../images/ai-customer-support-platform-with-langgraph/reimbursement-simulation-human-intervection.png" alt="Refund request forwarded to a human" width="900">

</details>

<details>
<summary>Support Console — inbox, takeover, and tool trail</summary>

A dark-themed console for the support team: live inbox, ticket list, and takeover.

<img src="../images/ai-customer-support-platform-with-langgraph/interface-portal-console-suport.png" alt="Support console inbox" width="900">

On an escalated ticket the agent sees the transcript, the order summary, and the trail of tools the assistant already ran before taking over.

<img src="../images/ai-customer-support-platform-with-langgraph/chat-console-suport_EN.png" alt="Human takeover with order context and tool trace" width="900">

<img src="../images/ai-customer-support-platform-with-langgraph/recent-chats.png" alt="Recent conversations in the console" width="900">

</details>

<details>
<summary>Observability — agent telemetry</summary>

Ticket volume, escalation rate, average confidence, run latency, intent mix, and per-tool error rate and p95 latency.

<img src="../images/ai-customer-support-platform-with-langgraph/analytics.png" alt="Analytics console with escalation rate, latency, and tool calls" width="900">

</details>

<details>
<summary>Security — jailbreak and prompt injection</summary>

Attempts to override the assistant's instructions are refused. It stays on policy and escalates rather than executing an unauthorized refund.

<img src="../images/ai-customer-support-platform-with-langgraph/jailbreak-simulation_EN.png" alt="Jailbreak attempt refused" width="900">

<img src="../images/ai-customer-support-platform-with-langgraph/prompt-injection-simulation-0.png" alt="Prompt injection attempt refused" width="900">

</details>

<details>
<summary>Deployment — DigitalOcean App Platform</summary>

The same stack split into separate services: FastAPI + LangGraph API, Next.js web, PostgreSQL with pgvector, Valkey for cache and chat pub/sub, and seed/ingest jobs for the synthetic data and knowledge base.

<img src="../images/ai-customer-support-platform-with-langgraph/deploy-components.png" alt="DigitalOcean App Platform components" width="900">

</details>

> [!NOTE]
> Setup instructions and environment variables live in the [project repository](https://github.com/OtnielGomes/AI-Customer-Support-Platform-With-Langgraph).

<p align="right">(<a href="#top">back to top</a>)</p>
