<a id="top"></a>

[← Back to portfolio](../README.md)

# AI Agent with Docker Containers and Python 🤖

[![LangGraph](https://img.shields.io/badge/LangGraph-agents-1C3C3C?style=flat-square)](https://www.langchain.com/langgraph)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Next.js%2016-000000?style=flat-square&logo=nextdotjs&logoColor=white)](https://nextjs.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)

**Repository:** [AI-Agent-with-Docker-Containers-and-Python](https://github.com/OtnielGomes/AI-Agent-with-Docker-Containers-and-Python)

<div align="center">
  <a href="https://github.com/OtnielGomes/AI-Agent-with-Docker-Containers-and-Python">
    <img src="../images/ai-agent-email/project_cover.png" alt="AI Agent with Docker project cover" width="900">
  </a>
</div>

**Problem:** An assistant that mails as soon as it finishes a draft will send the wrong recipient or the wrong text, and there is no step where a person can stop it. Reading the inbox and writing the message still has to be faster than doing both by hand.

**Solution:** A **LangGraph supervisor** routes each turn to a research worker, which writes the subject and a plain-text body, or to an email worker, which reads Gmail over IMAP, summarizes recent messages, and prepares an outbound draft. The **Next.js** UI keeps the inbox in the center of an empty conversation and opens a review card for every outbound message. **Confirm send** is the call that runs Gmail SMTP. **Discard** drops the card. A follow-up in the composer revises that same card instead of opening a second draft. **Reply** addresses the sender of the open message and ignores the recipient pinned in the sidebar.

**Result:** Inbox reading, drafting, in-place revision, reply, and confirm-before-send, with chat messages and drafts stored in **PostgreSQL**. Deployed on **DigitalOcean App Platform** as the API, the Next.js web app, and managed PostgreSQL.

## Architecture

```mermaid
flowchart TB
    UI[Next.js chat UI] -->|chat and inbox| API[FastAPI]
    API --> DB[(PostgreSQL)]
    API --> Supervisor[LangGraph supervisor]
    Supervisor --> Research[research_agent]
    Supervisor --> Email[email_agent]
    Research -->|research_email| LLM[OpenAI]
    Email -->|prepare draft| Draft[Draft card]
    Email -->|get_recent_emails| IMAP[Gmail IMAP]
    Draft --> DB
    UI -->|"Confirm send"| API
    API -->|SMTP| GmailSMTP[Gmail SMTP]
```

| Layer | Technology | Responsibility |
|-------|------------|----------------|
| API | FastAPI, uvicorn | HTTP, validation, persistence |
| Agents | LangGraph, langgraph-supervisor | Supervisor, research, and email |
| LLM | langchain-openai | Subject and plain-text body |
| Email | smtplib, IMAP | Send on confirm, read via Gmail |
| Database | SQLModel, PostgreSQL | Messages and drafts |
| UI | Next.js | Inbox, chat, review card, prompts |
| Containers | Docker Compose | Local stack and the production base |

## Demos

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
> Setup instructions and environment variables live in the [project repository](https://github.com/OtnielGomes/AI-Agent-with-Docker-Containers-and-Python).

<p align="right">(<a href="#top">back to top</a>)</p>
