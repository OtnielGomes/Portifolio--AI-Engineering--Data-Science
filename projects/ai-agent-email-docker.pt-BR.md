<a id="top"></a>

[← Voltar ao portfólio](../README.pt-BR.md)

**Idioma:** [English](ai-agent-email-docker.md) | Português

# Agente de e-mail com Docker Containers e Python 🤖

[![LangGraph](https://img.shields.io/badge/LangGraph-agents-1C3C3C?style=flat-square)](https://www.langchain.com/langgraph)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Next.js%2016-000000?style=flat-square&logo=nextdotjs&logoColor=white)](https://nextjs.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)

**Repositório:** [AI-Agent-with-Docker-Containers-and-Python](https://github.com/OtnielGomes/AI-Agent-with-Docker-Containers-and-Python)

<div align="center">
  <a href="https://github.com/OtnielGomes/AI-Agent-with-Docker-Containers-and-Python">
    <img src="covers/ai-agent-email-docker/cover.pt.png" alt="ai-agent-email-docker cover" width="900">
  </a>
</div>

| | |
|---|---|
| **Contexto** | Projeto de portfólio |
| **Linha do tempo** | 2025 — 2026 |
| **Foco** | Agentes LangGraph e human-in-the-loop |

LangGraph · FastAPI · Next.js · PostgreSQL · Docker · OpenAI

## Visão geral

Um assistente que dispara o e-mail assim que termina o rascunho pode errar destinatário ou texto, sem nenhuma etapa em que uma pessoa interrompa o envio. Ler a caixa de entrada e redigir ainda precisa ser mais rápido do que fazer tudo manualmente.

Um **supervisor LangGraph** encaminha cada turno para um worker de pesquisa (assunto e corpo em texto simples) ou para um worker de e-mail (Gmail via IMAP, resumos de mensagens recentes, rascunhos de saída). A interface **Next.js** mantém a inbox no centro da conversa vazia e abre um **card de revisão** para cada mensagem de saída. **Confirmar envio** é o único caminho para o SMTP do Gmail; **Descartar** remove o card. Novos pedidos no compositor **revisam o mesmo card**, sem segundo rascunho paralelo. **Responder** usa o remetente da mensagem aberta, não o endereço fixo na barra lateral.

Mensagens e rascunhos ficam no **PostgreSQL**. A stack roda localmente com Docker Compose e em produção no **DigitalOcean App Platform** (API, web, Postgres gerenciado).


## Arquitetura

Fluxo ponta a ponta do chat e da inbox até o envio só após confirmação.

![Diagrama de arquitetura](architecture-cases/ai-agent-email-docker-pt.png)

## Passo a passo da implementação

### FASE 01 — Requisições e estado da sessão

A camada FastAPI valida o payload do chat, carrega o histórico e persiste turnos de usuário e assistente no PostgreSQL (SQLModel). A UI chama a API por HTTP; credenciais do Gmail ficam só no servidor.

### FASE 02 — Roteamento do supervisor

O supervisor LangGraph classifica a mensagem e delega ao **research_agent** (redigir ou revisar conteúdo) ou ao **email_agent** (ler inbox, preparar rascunhos, resumir threads). Ferramentas separam leitura IMAP da criação de rascunhos.

### FASE 03 — Card de rascunho e revisão no lugar

O worker de e-mail devolve campos estruturados do rascunho. A API grava o rascunho e a UI mostra assunto, corpo, destinatário, **Confirmar envio** e **Descartar**. Um pedido de ajuste atualiza o mesmo registro—sem cards duplicados.

### FASE 04 — Envio só após confirmação

O SMTP só roda depois da confirmação explícita. Até lá, nada sai do servidor. No modo responder, o assunto ganha `Re:` e o destinatário é o remetente original, independente do pin na sidebar.

### FASE 05 — Containers e deploy

O Docker Compose liga API, Next.js e Postgres para paridade local. O App Platform da DigitalOcean executa os mesmos três componentes com banco gerenciado e logs de runtime.

## Stack em detalhe

### LangGraph

Supervisor e workers especializados com handoffs explícitos—mais testável que um único prompt monolítico.

### FastAPI

HTTP enxuto: validação, persistência e invocação dos agentes, sem expor credenciais de e-mail ao cliente.

### Next.js

UX com inbox em primeiro plano e cards de revisão; a ação perigosa nunca é o botão padrão.

### PostgreSQL

Estado durável de chat e rascunhos para revisão em vários passos sem perder contexto.

### Docker

Um comando sobe a stack inteira para demos e espelha a topologia de produção.

### OpenAI (via LangChain)

Gera assunto e corpo; o envio de mail continua em etapa separada e bloqueada.

## Demonstrações

<details>
<summary>Inbox, open, reply, and summarize</summary>

An empty conversation shows the inbox in the center. The sidebar pins **My inbox** or **Other recipient** and offers three example prompts.

![Home screen with the inbox in the center](../images/ai-agent-email/interface-inicial-en.png)

Opening a message shows the sender, subject, date, and plain-text body, with **Back** and **Reply**.

![Opened email with Back and Reply](../images/ai-agent-email/botao-responder-en.png)

**Reply** opens one draft whose subject starts with `Re:` and whose recipient is the sender. The address pinned in the sidebar stays out of that reply.

![Reply draft addressed to the sender](../images/ai-agent-email/teste-email-aberto-en.png)

*Summarize my last 3 emails* returns the sender and subject of the recent messages.

![Summary of the last three emails](../images/ai-agent-email/resumo-emails-en.png)

</details>

<details>
<summary>Draft, revise, and confirm send</summary>

A prompt such as *Write an email about artificial intelligence applied to business* comes back as a card: subject, body, recipient, **Confirm send**, and **Discard**. SMTP runs only on confirm.

![Prompt in the composer, with another recipient pinned](../images/ai-agent-email/teste-envio-email-en.png)

![Draft card ready to confirm or discard](../images/ai-agent-email/email-criado-en.png)

With the card open, a follow-up in the composer — shorten the body, change the subject — updates that same card. A second draft does not appear.

![Revision request in the composer](../images/ai-agent-email/editando-email-en.png)

![Same draft after the subject and body change](../images/ai-agent-email/editando-email-resposta-en.png)

After **Confirm send**, the thread shows the message as sent.

![Sent email after confirm](../images/ai-agent-email/confirmacao-envio-en.png)

</details>

<details>
<summary>Deployment — DigitalOcean App Platform</summary>

One Web App with three components: the API, the Next.js interface, and managed PostgreSQL.

![Deploy completed on DigitalOcean](../images/ai-agent-email/deploy-digital-ocean.png)

![API, web, and PostgreSQL in production](../images/ai-agent-email/interface_deploy_digital-ocean.png)

![Runtime logs on DigitalOcean](../images/ai-agent-email/runtimeslogs.png)

</details>

> [!NOTE]
> Instruções de setup e variáveis de ambiente estão no [repositório do projeto](https://github.com/OtnielGomes/AI-Agent-with-Docker-Containers-and-Python).

<p align="right">(<a href="#top">voltar ao topo</a>)</p>
