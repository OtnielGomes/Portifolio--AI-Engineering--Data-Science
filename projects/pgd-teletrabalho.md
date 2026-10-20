<a id="top"></a>

[← Back to portfolio](../README.md)

**Language:** English | [Português](pgd-teletrabalho.pt-BR.md)

# PGD Teletrabalho 📜

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Next.js%2015-000000?style=flat-square&logo=nextdotjs&logoColor=white)](https://nextjs.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-pgvector-4169E1?style=flat-square&logo=postgresql&logoColor=white)](https://github.com/pgvector/pgvector)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)
[![pytest](https://img.shields.io/badge/pytest-89%20passed-0A9B1D?style=flat-square)](https://docs.pytest.org/)

**Repository:** [Enterprise-Knowledge---RAG-Platform](https://github.com/OtnielGomes/Enterprise-Knowledge---RAG-Platform)

<div align="center">
  <a href="https://github.com/OtnielGomes/Enterprise-Knowledge---RAG-Platform">
    <img src="covers/pgd-teletrabalho/cover.en.png" alt="pgd-teletrabalho cover" width="900">
  </a>
</div>

RAG-Platform
imageDir: pgd-teletrabalho
tech:
  - Python
  - FastAPI
  - Next.js
  - PostgreSQL
  - Docker
  - pytest
---

# PGD Telework Assistant (Unifesp)

| | |
|---|---|
| **Context** | Independent portfolio |
| **Timeline** | 2025 — 2026 |
| **Focus area** | Citation gate & normative RAG |

Python · FastAPI · Next.js · PostgreSQL · Docker · pytest

## Overview

A technical-administrative servidor at Unifesp asking about telework cannot trust an unconstrained answer. The reply must cite the normative act in force, point to an article on the PDF page, and refuse when the corpus does not support the claim. A superseded resolution must not be treated as current, and an amendment must not be silently merged into the act it changes.

One product seam, **Ask**: lexical retrieval over a dated snapshot of five numbered acts, a Portuguese draft, then a **deterministic citation gate**. Default retrieval uses Current acts; Resolução CONSU 213/2021 enters only for historical questions. FastAPI owns Ask, Next.js is a single chat shell, PostgreSQL holds act and article metadata. The same Compose file runs locally and on a DigitalOcean droplet.

Every surviving claim cites a retrieved article, or the response is **Insufficient Evidence**. Corpus cutoff: **18 September 2026**. **89** pytest tests pass with extractive draft and empty `OPENAI_API_KEY`, including a **43**-item golden set scored through Ask.


## Architecture

Snapshot PDFs, lexical retrieve, draft, citation gate—no LLM judge on the request path.

![Architecture diagram](architecture-cases/pgd-teletrabalho-en.png)

## Implementation walkthrough

### PHASE 01 — Snapshot ingest and metadata

Five public PDFs (CONSU 262/2025, federal decrees and instructions, superseded 213/2021) are copied into the API image with a manifest. PostgreSQL stores act status (Current vs Superseded) and article text for retrieval and gate checks.

### PHASE 02 — Lexical retrieval

Default candidate set is Current acts only. Historical markers widen the set to include 213/2021. v1 uses lexical overlap on articles—not vector search on the hot path.

### PHASE 03 — Draft generation

`gpt-4o-mini` produces a Portuguese JSON draft when a key is present. Empty key or API failure falls back to an extractive draft. Retrieval and gate do not depend on the chat model.

### PHASE 04 — Deterministic citation gate

A citation survives only if its `article_id` was retrieved or its quote appears in article text. Fabricated citations drop. If none remain, the API returns Insufficient Evidence—no LLM-as-judge.

### PHASE 05 — Tests, CI, and deploy

Golden-set categories (temporal, historical, unanswerable, amendment conflict) run through Ask. CI executes the same **89** tests without OpenAI secrets. Production uses the same `compose.yaml` as local dev.

## Tech stack deep-dive

### FastAPI (`Ask` API)

Single seam for retrieve → draft → gate keeps the contract testable end-to-end.

### Lexical retrieval

Predictable behavior for a small, versioned legal slice beats embedding search before you have eval coverage.

### Citation gate (Python)

Trust is enforced in code; the model only proposes text and citations to be verified.

### Next.js chat shell

Portuguese UI proxies Ask and serves PDFs at cited pages.

### PostgreSQL + pgvector (runtime slice)

Metadata store today; pgvector is in the stack but not on the v1 request path.

### Docker Compose

Local and droplet parity—one file, health checks, snapshot cutoff visible in ops.

## Screenshots

The running chat is Portuguese only. The English shots below document the same flows.

<details>
<summary>How it answers — current, historical, and refusal</summary>

A question about a rule in force is answered from Current acts. Here both a Unifesp act and a federal instruction speak, so both citations survive: participation in telework is not an acquired right.

<img src="../images/pgd-teletrabalho/regra-vigente-en.png" alt="Current rule: participation is not an acquired right, citing CONSU Resolution 262/2025 art. 19 and IN conjunta 24/2023 art. 15" width="900">

Questions about when an act entered into force stay on the Current slice. The cutoff is the snapshot date, not today. Resolution 262 comes into effect on 3 February 2025.

<img src="../images/pgd-teletrabalho/vigente-temporal-en.png" alt="When Resolution 262 comes into effect: 3 February 2025, citing art. 48" width="900">

A historical question is the only case in which the superseded Resolução CONSU 213/2021 may be cited.

<img src="../images/pgd-teletrabalho/historicas-en.png" alt="Historical question: the 2021 resolution prohibited housing assistance in full-time telework, citing art. 40" width="900">

Questions outside the snapshot are refused. The assistant does not guess.

<img src="../images/pgd-teletrabalho/sem-evidencias-en.png" alt="Out-of-slice question about the IOF rate: Insufficient Evidence refusal" width="900">

</details>

<details>
<summary>Deployment — the same Compose file on a droplet</summary>

The droplet runs the same `compose.yaml` as local development. PostgreSQL and Ask listen on localhost; the chat is the published port.

<img src="../images/pgd-teletrabalho/deploy-1.png" alt="SSH session starting docker compose up on the droplet" width="900">

<img src="../images/pgd-teletrabalho/deploy-2.png" alt="Compose services healthy and health check reporting cutoff 2026-09-18" width="900">

<img src="../images/pgd-teletrabalho/interface-deploy.png" alt="DigitalOcean droplet overview for the pgd-teletrabalho instance" width="900">

</details>

<details>
<summary>Tests — golden set through Ask</summary>

`pytest` in `api/` collected **89** tests and passed all of them with the extractive draft and an empty API key. CI runs that same suite: no OpenAI secret, no Langfuse, no RAGAS.

<img src="../images/pgd-teletrabalho/tests.png" alt="pytest session: 89 passed" width="900">

</details>

> [!NOTE]
> Setup instructions and environment variables live in the [project repository](https://github.com/OtnielGomes/Enterprise-Knowledge---RAG-Platform).

<p align="right">(<a href="#top">back to top</a>)</p>
