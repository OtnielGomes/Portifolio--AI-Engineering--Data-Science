<a id="top"></a>

[← Voltar ao portfólio](../README.pt-BR.md)

**Idioma:** [English](ai-customer-support-platform.md) | Português

# AI Customer Support Platform 🎧

[![LangGraph](https://img.shields.io/badge/LangGraph-supervisor-1C3C3C?style=flat-square)](https://www.langchain.com/langgraph)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Next.js%2016-000000?style=flat-square&logo=nextdotjs&logoColor=white)](https://nextjs.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-pgvector-4169E1?style=flat-square&logo=postgresql&logoColor=white)](https://github.com/pgvector/pgvector)
[![Redis](https://img.shields.io/badge/Redis-pub%2Fsub-DC382D?style=flat-square&logo=redis&logoColor=white)](https://redis.io/)
[![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-Langfuse-425CC7?style=flat-square&logo=opentelemetry&logoColor=white)](https://opentelemetry.io/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)

**Repositório:** [AI-Customer-Support-Platform-With-Langgraph](https://github.com/OtnielGomes/AI-Customer-Support-Platform-With-Langgraph)

<div align="center">
  <a href="https://github.com/OtnielGomes/AI-Customer-Support-Platform-With-Langgraph">
    <img src="covers/ai-customer-support-platform/cover.pt.png" alt="ai-customer-support-platform cover" width="900">
  </a>
</div>

| | |
|---|---|
| **Contexto** | Projeto de portfólio |
| **Linha do tempo** | 2025 — 2026 |
| **Foco** | Multiagente, motor de políticas e RAG |

LangGraph · FastAPI · Next.js · PostgreSQL/pgvector · Redis · Langfuse · Docker

## Visão geral

Um assistente de suporte que fala de pedidos precisa acertar os fatos. Tem que responder *quando chega meu pacote* a partir da linha real de envio, negar reembolso fora da política e passar a conversa para um humano quando a automação não tem mandato. Um LLM que improvisa só com contexto inventa status de pedido e aprova reembolsos indevidos.

Um **supervisor LangGraph** classifica a intenção e delega a workers de cobrança, logística ou conta. Três fontes da verdade permanecem separadas: **PostgreSQL** para fatos operacionais, **motor de políticas determinístico** (`company.yaml`) para dinheiro e prazos, e **RAG em pgvector** para procedimentos e FAQ—linhas operacionais ficam de fora do índice de propósito. Ferramentas respeitam o cliente autenticado; o BFF **Next.js** impede que chaves de API cheguem ao navegador.

O produto entrega **Portal do Cliente** e **Console de Suporte** com chat ao vivo via SSE, takeover humano na mesma thread, guardrails contra jailbreak e injeção de prompt, e console analítico com OpenTelemetry e Langfuse. Deploy no **DigitalOcean App Platform** (API, web, Postgres/pgvector, Valkey).


## Arquitetura

Supervisor, agentes de domínio, fatos, política e conhecimento—sem colapsar tudo no prompt.

![Diagrama de arquitetura](architecture-cases/ai-customer-support-platform-pt.png)

## Passo a passo da implementação

### FASE 01 — Autenticação e BFF

Login só por e-mail no portal; endereços desconhecidos são rejeitados. O Next.js encaminha chat e tickets por um backend-for-frontend, sem expor segredos no cliente.

### FASE 02 — Guardrails e entrada no grafo

Mensagens passam por checagens de segurança antes do workflow LangGraph. Falhas desviam para recusa ou escalonamento.

### FASE 03 — Supervisor e ferramentas com escopo

O supervisor escolhe cobrança, logística, conta ou escalonamento. Ferramentas (`get_order`, `get_payments`, `get_shipment`, `check_refund_eligibility`) ficam amarradas ao ID do cliente do ticket.

### FASE 04 — Política, RAG e banco

Fatos vêm de consultas SQL. Regras de reembolso e limites em BRL são avaliadas em Python antes de qualquer ação destrutiva. O RAG busca *explicações* de política em `data/knowledge_base/`, não linhas vivas de pedido.

### FASE 05 — Chat ao vivo, takeover e observabilidade

Redis pub/sub distribui tokens SSE; mensagens persistem para um humano assumir no meio da thread. Escalonamento pausa a automação enquanto o console mostra o rastro de ferramentas. Langfuse e OpenTelemetry alimentam dashboards de intenção, latência e erro por tool.

## Stack em detalhe

### LangGraph

Grafo supervisor/worker espelha como times de suporte pensam intenção e repasse.

### Motor de políticas (YAML + Python)

Valores que custam dinheiro se errados não são negociáveis em prompt de sistema.

### RAG com pgvector

Responde procedimento mantendo dado transacional no SQL.

### Redis / Valkey

Cache e pub/sub para chat responsivo e console em tempo real.

### Langfuse + OpenTelemetry

Tracing de produção para evals (intenção, chamada de tool, conformidade com política).

### Docker e GitHub Actions

Mundo sintético reproduzível (anomalias `SCN-*`) para demo e regressão.

## Capturas de tela

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

> [!NOTE]
> Instruções de setup e variáveis de ambiente estão no [repositório do projeto](https://github.com/OtnielGomes/AI-Customer-Support-Platform-With-Langgraph).

<p align="right">(<a href="#top">voltar ao topo</a>)</p>
