<a id="top"></a>

[← Back to portfolio](../README.md)

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
    <img src="../images/ai-customer-support-platform-with-langgraph/project_cover.png" alt="AI Customer Support Platform project cover" width="900">
  </a>
</div>

**Problem:** A support assistant that talks about orders has to be right about them. It needs to answer *when will my package arrive* from the actual shipment row, refuse a refund the policy does not allow, and hand the conversation to a human when the case exceeds what automation is authorized to do. An LLM asked to do this from context alone will confidently invent order states and approve refunds it should not.

**Solution:** A **LangGraph supervisor** classifies each ticket's intent and delegates to billing, logistics, or account workers. Those workers read from three separate sources of truth: **PostgreSQL** for operational facts, a **deterministic policy engine** for anything with money or deadlines attached, and **RAG over pgvector** for the procedures and FAQs that explain policy. Tools are scoped to the authenticated customer, and the **Next.js** front end reaches the API through a BFF so keys never touch the browser.

**Result:** A two-surface product — Customer Portal and Support Console — where business rules live in code rather than in prompts, escalation pauses automation for a human takeover in the same thread, and jailbreak and prompt-injection attempts are refused instead of executed. Deployed on **DigitalOcean App Platform** as separate API, web, PostgreSQL/pgvector, and Valkey services, with OpenTelemetry and Langfuse tracing behind an analytics console.

## The three sources of truth

This separation is the core design decision of the project, and the reason the assistant does not hallucinate order state.

| Source | Holds | Why it is separate |
|---|---|---|
| **PostgreSQL** | Customers, orders, payments, shipments, tickets | Facts are read, never generated. The model asks a tool; it does not recall. |
| **Policy engine** (`app/policies/`, `data/company/company.yaml`) | Refund windows, BRL approval thresholds, shipping rules | Numbers that cost money when wrong belong in Python, evaluated before the model acts — not in a prompt the model can be talked out of. |
| **RAG over pgvector** (`data/knowledge_base/`) | Procedures, FAQs, policy explanations | Documents explain *why* a rule exists. Operational rows are deliberately kept out of the index. |

## Architecture

```mermaid
flowchart TD
    Browser[Next.js UI + BFF] --> API[FastAPI routes]
    API --> Guard[Guardrails]
    Guard --> Graph[LangGraph workflow]
    Graph --> Supervisor[Supervisor]
    Supervisor --> Billing[Billing agent]
    Supervisor --> Logistics[Logistics agent]
    Supervisor --> Account[Account agent]
    Supervisor --> Escalation[Escalation agent]
    Billing --> Tools[Scoped tools]
    Logistics --> Tools
    Account --> Tools
    Billing --> RAG[pgvector RAG]
    Billing --> Policy[Policy engine]
    Tools --> DB[(PostgreSQL facts)]
    RAG --> KB[Policy documents]
    Policy --> YAML[company.yaml]
    Escalation --> Human[Support console takeover]
    API --> Redis[(Redis cache + pub/sub)]
```

| Layer | Technology |
|---|---|
| API | FastAPI, Pydantic, Uvicorn |
| Agents | LangGraph — supervisor plus domain workers |
| LLM | OpenAI-compatible, configured via environment |
| RAG | PostgreSQL + pgvector |
| Cache / live events | Redis, Valkey in the cloud |
| Observability | OpenTelemetry, Langfuse |
| Frontend | Next.js 16 — Customer Portal and Support Console |
| Infrastructure | Docker, Docker Compose, GitHub Actions |

### Scoped tools

Every tool is bound to the ticket's customer, so a worker cannot read another customer's data even if the conversation tries to steer it there.

| Tool | Returns |
|---|---|
| `get_order` | Order header, items, and current state |
| `get_payments` | Payment attempts, including duplicate charges |
| `get_shipment` | Carrier, tracking, and estimated delivery |
| `check_refund_eligibility` | Policy verdict with the rule that produced it |

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

## Engineering notes

- **Synthetic world, reproducible demos.** Customers, orders, and payments are generated from a seeded profile with labeled anomalies (`SCN-*`) — double charges, delayed shipments, refunds outside the window — so a scenario can be replayed exactly for evaluation.
- **Live chat over SSE.** Token streaming with Redis pub/sub fan-out and persisted `ticket_messages`, which is what lets a human pick up a conversation mid-thread.
- **Evaluation harness.** `app/evaluation/` defines datasets and evaluators for intent accuracy, tool-call correctness, policy compliance, and unauthorized-action rate.

> [!NOTE]
> Setup instructions, environment variables, and demo logins live in the [project repository](https://github.com/OtnielGomes/AI-Customer-Support-Platform-With-Langgraph), which also has a [Portuguese README](https://github.com/OtnielGomes/AI-Customer-Support-Platform-With-Langgraph/blob/main/README.pt-BR.md).

<p align="right">(<a href="#top">back to top</a>)</p>
