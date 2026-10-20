"""One-off builder: merge projects-cases into public project pages."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "projects" / "projects-cases"
PUB = ROOT / "projects"

SLUGS = [
    "nfe-document-extraction",
    "ai-customer-support-platform",
    "ai-agent-email-docker",
    "pgd-teletrabalho",
    "churn-prediction-credit-card",
    "credit-risk-classification",
]

META: dict[str, dict] = {
    "nfe-document-extraction": {
        "title_en": "# NFe Document Extraction 📄",
        "title_pt": "# Extração de documentos NFe 📄",
        "repo_line_en": "**Repository:** [NFe-Document-Extraction](https://github.com/OtnielGomes/NFe-Document-Extraction)",
        "repo_line_pt": "**Repositório:** [NFe-Document-Extraction](https://github.com/OtnielGomes/NFe-Document-Extraction)",
        "repo_url": "https://github.com/OtnielGomes/NFe-Document-Extraction",
        "badges": """[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langchain&logoColor=white)](https://www.langchain.com/langgraph)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white)](https://openai.com/)
[![LangSmith](https://img.shields.io/badge/LangSmith-1C3C3C?style=flat-square&logo=langchain&logoColor=white)](https://smith.langchain.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)""",
        "legacy_marker": "## Screenshots",
        "legacy_stop": None,
        "nfe_metrics": True,
    },
    "ai-customer-support-platform": {
        "title_en": "# AI Customer Support Platform 🎧",
        "title_pt": "# AI Customer Support Platform 🎧",
        "repo_line_en": "**Repository:** [AI-Customer-Support-Platform-With-Langgraph](https://github.com/OtnielGomes/AI-Customer-Support-Platform-With-Langgraph)",
        "repo_line_pt": "**Repositório:** [AI-Customer-Support-Platform-With-Langgraph](https://github.com/OtnielGomes/AI-Customer-Support-Platform-With-Langgraph)",
        "repo_url": "https://github.com/OtnielGomes/AI-Customer-Support-Platform-With-Langgraph",
        "badges": """[![LangGraph](https://img.shields.io/badge/LangGraph-supervisor-1C3C3C?style=flat-square)](https://www.langchain.com/langgraph)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Next.js%2016-000000?style=flat-square&logo=nextdotjs&logoColor=white)](https://nextjs.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-pgvector-4169E1?style=flat-square&logo=postgresql&logoColor=white)](https://github.com/pgvector/pgvector)
[![Redis](https://img.shields.io/badge/Redis-pub%2Fsub-DC382D?style=flat-square&logo=redis&logoColor=white)](https://redis.io/)
[![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-Langfuse-425CC7?style=flat-square&logo=opentelemetry&logoColor=white)](https://opentelemetry.io/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)""",
        "legacy_marker": "## Screenshots",
        "legacy_stop": "## Engineering notes",
    },
    "ai-agent-email-docker": {
        "title_en": "# AI Agent with Docker Containers and Python 🤖",
        "title_pt": "# Agente de e-mail com Docker Containers e Python 🤖",
        "repo_line_en": "**Repository:** [AI-Agent-with-Docker-Containers-and-Python](https://github.com/OtnielGomes/AI-Agent-with-Docker-Containers-and-Python)",
        "repo_line_pt": "**Repositório:** [AI-Agent-with-Docker-Containers-and-Python](https://github.com/OtnielGomes/AI-Agent-with-Docker-Containers-and-Python)",
        "repo_url": "https://github.com/OtnielGomes/AI-Agent-with-Docker-Containers-and-Python",
        "badges": """[![LangGraph](https://img.shields.io/badge/LangGraph-agents-1C3C3C?style=flat-square)](https://www.langchain.com/langgraph)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Next.js%2016-000000?style=flat-square&logo=nextdotjs&logoColor=white)](https://nextjs.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)""",
        "legacy_marker": "## Demos",
        "legacy_stop": "> [!NOTE]",
        "legacy_title_pt": "## Demonstrações",
    },
    "pgd-teletrabalho": {
        "title_en": "# PGD Teletrabalho 📜",
        "title_pt": "# PGD Teletrabalho 📜",
        "repo_line_en": "**Repository:** [Enterprise-Knowledge---RAG-Platform](https://github.com/OtnielGomes/Enterprise-Knowledge---RAG-Platform)",
        "repo_line_pt": "**Repositório:** [Enterprise-Knowledge---RAG-Platform](https://github.com/OtnielGomes/Enterprise-Knowledge---RAG-Platform)",
        "repo_url": "https://github.com/OtnielGomes/Enterprise-Knowledge---RAG-Platform",
        "badges": """[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Next.js%2015-000000?style=flat-square&logo=nextdotjs&logoColor=white)](https://nextjs.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-pgvector-4169E1?style=flat-square&logo=postgresql&logoColor=white)](https://github.com/pgvector/pgvector)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)
[![pytest](https://img.shields.io/badge/pytest-89%20passed-0A9B1D?style=flat-square)](https://docs.pytest.org/)""",
        "legacy_marker": "## Screenshots",
        "legacy_stop": "> [!NOTE]",
        "legacy_title_pt": "## Capturas de tela",
    },
    "churn-prediction-credit-card": {
        "title_en": "# Credit Card Churn Prediction 💳",
        "title_pt": "# Previsão de churn de cartão de crédito 💳",
        "repo_line_en": "**Repository:** [Churn-Prediction-Credit-Card](https://github.com/OtnielGomes/Churn-Prediction-Credit-Card)",
        "repo_line_pt": "**Repositório:** [Churn-Prediction-Credit-Card](https://github.com/OtnielGomes/Churn-Prediction-Credit-Card)",
        "repo_url": "https://github.com/OtnielGomes/Churn-Prediction-Credit-Card",
        "badges": """[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-boosting-01BFFF?style=flat-square)](https://xgboost.ai/)
[![LightGBM](https://img.shields.io/badge/LightGBM-boosting-0078D4?style=flat-square)](https://lightgbm.readthedocs.io/)""",
        "legacy_marker": "## CRISP-DM methodology",
        "legacy_stop": "<p align=\"right\">",
    },
    "credit-risk-classification": {
        "title_en": "# Credit Risk Classification 💸",
        "title_pt": "# Classificação de risco de crédito 💸",
        "repo_line_en": "**Repository:** [0_Portfolio-Credit_Risk_Analysis_with_Pytorch](https://github.com/OtnielGomes/0_Portfolio-Credit_Risk_Analysis_with_Pytorch)",
        "repo_line_pt": "**Repositório:** [0_Portfolio-Credit_Risk_Analysis_with_Pytorch](https://github.com/OtnielGomes/0_Portfolio-Credit_Risk_Analysis_with_Pytorch)",
        "repo_url": "https://github.com/OtnielGomes/0_Portfolio-Credit_Risk_Analysis_with_Pytorch",
        "badges": """[![PyTorch](https://img.shields.io/badge/PyTorch-neural%20nets-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Azure](https://img.shields.io/badge/Azure-Databricks-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)](https://azure.microsoft.com/)""",
        "legacy_marker": "## Risk classification levels",
        "legacy_stop": "<p align=\"right\">",
        "legacy_title_pt": "## Níveis de classificação de risco",
    },
}

NFE_METRICS_EN = """
## How the metrics chose the design

The first pass compared four extraction approaches on a sample of 10 synthetic invoices per row. Pricing table date: **2026-10-03**. Baseline, cheap vision, and the text layer used `gpt-4.1-mini-2025-04-14`. Strong vision used `gpt-4.1-2025-04-14`. That pass kept section agents plus the deterministic validator, and kept cheap vision: it reads a simulated photo, which the text layer cannot, and it costs less than strong vision.

| Pass | Rendition | Field accuracy | Cost per invoice (USD) | Errors reaching human review |
|---|---|---:|---:|---:|
| First test, cheap vision | digital PDF | 0.9721 | 0.007105 | 9 |
| First test, cheap vision | simulated photo | 0.5736 | 0.008941 | 8 |

The second pass kept cheap vision and compared `gpt-4.1-mini-2025-04-14` with `gpt-6-luna` (Responses API, reasoning effort none). LangSmith traces and the same metrics selected `gpt-6-luna`. Pricing table date: **2026-10-08**. The adopted rows are the cheap-vision rows.

| Pass | Rendition | Field accuracy | Cost per invoice (USD) | Errors reaching human review | Planted-error detection rate |
|---|---|---:|---:|---:|---:|
| Adopted, cheap vision | digital PDF | 0.9870 | 0.002035 | 8 | 1.0000 |
| Adopted, cheap vision | simulated photo | 0.6420 | 0.002367 | 9 | 1.0000 |

On the adopted sample, digital field accuracy rose from 0.9721 to 0.9870 and cost fell from US$ 0.007105 to US$ 0.002035. Simulated-photo field accuracy rose from 0.5736 to 0.6420. The full adopted table, including the other approaches, is in the source repository.
"""

NFE_METRICS_PT = """
## Como as métricas escolheram o desenho

A primeira passagem comparou quatro abordagens de extração em uma amostra de 10 notas sintéticas por linha. Data da tabela de preços: **2026-10-03**. Baseline, visão barata e camada de texto usaram `gpt-4.1-mini-2025-04-14`. Visão forte usou `gpt-4.1-2025-04-14`. Essa passagem mantém agentes por seção e o validador determinístico, e mantém visão barata: ela lê foto simulada, o que a camada de texto não cobre, e custa menos que visão forte.

| Passagem | Mídia | Acurácia de campo | Custo por nota (USD) | Erros que chegam à revisão humana |
|---|---|---:|---:|---:|
| Primeiro teste, visão barata | PDF digital | 0,9721 | 0,007105 | 9 |
| Primeiro teste, visão barata | foto simulada | 0,5736 | 0,008941 | 8 |

A segunda passagem mantém visão barata e compara `gpt-4.1-mini-2025-04-14` com `gpt-6-luna` (Responses API, reasoning effort none). Traces no LangSmith e as mesmas métricas escolheram `gpt-6-luna`. Data da tabela de preços: **2026-10-08**. As linhas adotadas são as de visão barata.

| Passagem | Mídia | Acurácia de campo | Custo por nota (USD) | Erros na revisão humana | Detecção de erro plantado |
|---|---|---:|---:|---:|---:|
| Adotada, visão barata | PDF digital | 0,9870 | 0,002035 | 8 | 1,0000 |
| Adotada, visão barata | foto simulada | 0,6420 | 0,002367 | 9 | 1,0000 |

Na amostra adotada, a acurácia em PDF digital subiu de 0,9721 para 0,9870 e o custo caiu de US$ 0,007105 para US$ 0,002035. Em foto simulada, a acurácia subiu de 0,5736 para 0,6420. A tabela completa adotada, incluindo as outras abordagens, está no repositório fonte.
"""


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return text
    end = text.find("---", 3)
    if end == -1:
        return text
    return text[end + 3 :].lstrip()


def drop_leading_h1(text: str) -> str:
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        return "\n".join(lines[1:]).lstrip()
    return text


def fix_architecture_image(text: str, slug: str, locale: str) -> str:
    suffix = "en" if locale == "en" else "pt"
    alt = "Architecture diagram" if locale == "en" else "Diagrama de arquitetura"
    replacement = f"![{alt}](architecture-cases/{slug}-{suffix}.png)"
    return re.sub(r"!\[[^\]]*\]\([^)]*architecture[^)]*\)", replacement, text)


def resolve_image_path(path: str) -> str:
    """Prefer Portuguese screenshot variants when building PT pages."""
    rel = path.replace("../", "")
    full = ROOT / rel
    if full.exists():
        return path
    for candidate in (
        path.replace("_EN.png", ".png"),
        path.replace("-en.png", ".png"),
        path.replace("_EN.", "."),
    ):
        if (ROOT / candidate.replace("../", "")).exists():
            return candidate
    return path


def localize_images_pt(section: str) -> str:
    def repl(match: re.Match[str]) -> str:
        prefix, path, suffix = match.group(1), match.group(2), match.group(3)
        return f"{prefix}{resolve_image_path(path)}{suffix}"

    section = re.sub(r'(\!\[[^\]]*\]\()([^)]+)(\))', repl, section)
    section = re.sub(r'(<img src=")([^"]+)(")', lambda m: f'{m.group(1)}{resolve_image_path(m.group(2))}{m.group(3)}', section)
    return section


def extract_legacy(legacy_path: Path, marker: str, stop: str | None) -> str:
    if not legacy_path.exists():
        return ""
    text = legacy_path.read_text(encoding="utf-8")
    idx = text.find(marker)
    if idx == -1:
        return ""
    chunk = text[idx:]
    if stop:
        stop_idx = chunk.find(stop)
        if stop_idx != -1:
            chunk = chunk[:stop_idx].rstrip()
    return chunk.strip()


def pgd_pt_screenshots(section: str) -> str:
    section = section.replace("-en.png", ".png")
    section = section.replace(
        "The running chat is Portuguese only. The English shots below document the same flows.",
        "O chat em execução é em português. As capturas abaixo documentam os mesmos fluxos.",
    )
    return section


def email_pt_screenshots(section: str) -> str:
    section = section.replace("## Demos", "## Demonstrações")
    return localize_images_pt(section)


def nfe_pt_screenshots(section: str) -> str:
    section = section.replace("## Screenshots", "## Capturas de tela")
    section = localize_images_pt(section)
    return section


def support_pt_screenshots(section: str) -> str:
    section = section.replace("## Screenshots", "## Capturas de tela")
    return localize_images_pt(section)


def build_page(slug: str, locale: str) -> str:
    meta = META[slug]
    case_file = CASES / slug / ("en.md" if locale == "en" else "pt.md")
    body = strip_frontmatter(case_file.read_text(encoding="utf-8"))
    body = drop_leading_h1(body)
    body = fix_architecture_image(body, slug, locale)
    # Remove duplicate repository line from body (we show it in header)
    body = re.sub(r"\n\*\*(Repository|Repositório):\*\*[^\n]+\n", "\n", body, count=1)

    cover = f"covers/{slug}/cover.{locale if locale == 'en' else 'pt'}.png"
    if locale == "pt":
        cover = f"covers/{slug}/cover.pt.png"
    else:
        cover = f"covers/{slug}/cover.en.png"

    if locale == "en":
        nav = "[← Back to portfolio](../README.md)\n\n**Language:** English | [Português]({slug}.pt-BR.md)".format(slug=slug)
        title = meta["title_en"]
        repo = meta["repo_line_en"]
        footer = '(<a href="#top">back to top</a>)'
        note_setup = "> [!NOTE]\n> Setup instructions and environment variables live in the [project repository]({url}).".format(
            url=meta["repo_url"]
        )
    else:
        nav = "[← Voltar ao portfólio](../README.pt-BR.md)\n\n**Idioma:** [English]({slug}.md) | Português".format(slug=slug)
        title = meta["title_pt"]
        repo = meta["repo_line_pt"]
        footer = '(<a href="#top">voltar ao topo</a>)'
        note_setup = "> [!NOTE]\n> Instruções de setup e variáveis de ambiente estão no [repositório do projeto]({url}).".format(
            url=meta["repo_url"]
        )

    legacy_path = PUB / f"{slug}.md"
    legacy = extract_legacy(legacy_path, meta["legacy_marker"], meta.get("legacy_stop"))
    if locale == "pt" and legacy:
        if slug == "pgd-teletrabalho":
            legacy = pgd_pt_screenshots(legacy)
            if meta.get("legacy_title_pt"):
                legacy = legacy.replace(meta["legacy_marker"], meta["legacy_title_pt"], 1)
        elif slug == "ai-agent-email-docker":
            legacy = email_pt_screenshots(legacy)
        elif slug == "nfe-document-extraction":
            legacy = nfe_pt_screenshots(legacy)
        elif slug == "ai-customer-support-platform":
            legacy = support_pt_screenshots(legacy)
        elif meta.get("legacy_title_pt"):
            legacy = legacy.replace(meta["legacy_marker"], meta["legacy_title_pt"], 1)

    extra = ""
    if meta.get("nfe_metrics"):
        extra = NFE_METRICS_EN if locale == "en" else NFE_METRICS_PT

    parts = [
        "<a id=\"top\"></a>",
        "",
        nav,
        "",
        title,
        "",
        meta["badges"],
        "",
        repo,
        "",
        f'<div align="center">\n  <a href="{meta["repo_url"]}">\n    <img src="{cover}" alt="{slug} cover" width="900">\n  </a>\n</div>',
        "",
        body.strip(),
    ]
    if extra:
        parts.extend(["", extra.strip()])
    if legacy:
        parts.extend(["", legacy])
    if slug in ("ai-agent-email-docker", "pgd-teletrabalho", "ai-customer-support-platform"):
        parts.extend(["", note_setup])
    parts.extend(["", f'<p align="right">{footer}</p>', ""])

    return "\n".join(parts)


def main() -> None:
    for slug in SLUGS:
        en_out = PUB / f"{slug}.md"
        pt_out = PUB / f"{slug}.pt-BR.md"
        en_out.write_text(build_page(slug, "en"), encoding="utf-8", newline="\n")
        pt_out.write_text(build_page(slug, "pt"), encoding="utf-8", newline="\n")
        print(f"Wrote {en_out.name} and {pt_out.name}")


if __name__ == "__main__":
    main()
