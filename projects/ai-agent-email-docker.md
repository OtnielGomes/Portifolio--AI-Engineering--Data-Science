<a id="top"></a>

[← Back to portfolio](../README.md)

# AI Agent with Docker Containers and Python 🤖

[![LangGraph](https://img.shields.io/badge/LangGraph-agents-1C3C3C?style=flat-square)](https://www.langchain.com/langgraph)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)

**Repository:** [AI-Agent-with-Docker-Containers-and-Python](https://github.com/OtnielGomes/AI-Agent-with-Docker-Containers-and-Python)

<div align="center">
  <a href="https://github.com/OtnielGomes/AI-Agent-with-Docker-Containers-and-Python">
    <img src="../images/ai-agent_email/project_cover.png" alt="AI Agent with Docker project cover" width="900">
  </a>
</div>

**Problem:** Manual email workflows — researching topics, reading the inbox, and drafting replies — are slow and repetitive.

**Solution:** A **LangGraph multi-agent** assistant with a supervisor routing tasks to research and email workers. **FastAPI** handles the API, **PostgreSQL** stores chat history, **Streamlit** provides the UI, and **Docker Compose** packages everything for local and cloud deployment.

**Result:** End-to-end assistant deployed on **DigitalOcean App Platform**, capable of summarizing inbox messages and sending structured emails via Gmail.

## Architecture

```mermaid
flowchart TB
    UI[Streamlit frontend] -->|POST /api/chats/| API[FastAPI]
    Client[HTTP client] -->|POST /api/chats/| API
    API --> DB[(PostgreSQL)]
    API --> Supervisor[LangGraph supervisor]
    Supervisor --> Research[research_agent]
    Supervisor --> Email[email_agent]
    Research -->|research_email| LLM[OpenAI]
    Email -->|send_me_email| SMTP[Gmail SMTP]
    Email -->|get_recent_emails| IMAP[Gmail IMAP]
    Supervisor --> API
    API --> UI
    API --> Client
```

| Layer | Technology | Responsibility |
|-------|------------|----------------|
| API | FastAPI, uvicorn | HTTP routes, validation, persistence |
| Agents | LangGraph, langgraph-supervisor | Supervisor + workers (research, email) |
| LLM | langchain-openai | Structured email generation |
| Email | smtplib, IMAP | Send and read via Gmail |
| Database | SQLModel, PostgreSQL | Chat message history |
| UI | Streamlit | Chat, recipient settings, prompts |
| Containers | Docker Compose | Local orchestration and production base |

## Demos

<details>
<summary>View demos, deployment, and observability</summary>

### Agent interface

Sidebar with connection test, recipient choice (*send to myself* or *other email*), and pre-built prompts.

![Agent interface](../images/ai-agent_email/interface_of_agent.png)

### Summarize recent emails

Request: *"Summarize my last 3 emails."* — the agent reads the inbox and returns a structured summary.

![Email summarization test](../images/ai-agent_email/test_of__prompt_summarize-emails.png)

### Schedule a meeting by email

Request: *"Help me write an email to schedule a meeting for this week."*

<table>
  <tr>
    <td width="50%"><img src="../images/ai-agent_email/test_send_email_1.png" alt="Meeting scheduling prompt" /></td>
    <td width="50%"><img src="../images/ai-agent_email/result_of_test_send_email_1.png" alt="Meeting email result" /></td>
  </tr>
</table>

### Email about Artificial Intelligence

Request: *"Write me an email about artificial intelligence applied to business."*

<table>
  <tr>
    <td width="50%"><img src="../images/ai-agent_email/test_send_email_2.png" alt="AI prompt" /></td>
    <td width="50%"><img src="../images/ai-agent_email/result_of_test_send_email_2.png" alt="AI email result" /></td>
  </tr>
</table>

### Deployment on DigitalOcean

![DigitalOcean deployment](../images/ai-agent_email/deploy-digital-ocean.png)

![Deployed interface](../images/ai-agent_email/interface_deploy_digital-ocean.png)

### Runtime logs

![Runtime logs](../images/ai-agent_email/runtimeslogs.png)

</details>

<p align="right">(<a href="#top">back to top</a>)</p>
