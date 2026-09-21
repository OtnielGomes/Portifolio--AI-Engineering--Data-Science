<a id="readme-top"></a>

<div align="center">
  <a href="https://github.com/OtnielGomes/Portifolio--AI-Engineering--Data-Science">
    <img src="images/ia_engineer.png" alt="Portfólio de AI Engineer" width="900">
  </a>

  <h1>Portfólio de AI Engineer</h1>

  <p><strong>Otniel Gomes</strong> — construo e avalio sistemas baseados em LLM<br />com qualidade, latência e observabilidade mensuráveis.</p>

  **Idioma:** [English](README.md) | Português

  [![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
  [![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://www.langchain.com/langgraph)
  [![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
  [![RAGAS](https://img.shields.io/badge/RAGAS-6366F1?style=for-the-badge)](https://docs.ragas.io/)
  [![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)](https://pytorch.org)
  [![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
  [![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5.svg?style=for-the-badge&logo=linkedin&colorB=0077B5)](https://linkedin.com/in/otnielgomes)
</div>

---

Pipelines de RAG, assistentes multi-agente e frameworks de benchmark — construídos para que as afirmações interessantes possam ser verificadas. Regras de negócio ficam no código, não no prompt; a qualidade da recuperação é medida em vez de presumida; e cada projeto aqui aponta para o repositório que o originou.

Aberto a oportunidades e colaborações em **AI Engineering, sistemas com LLM e IA Generativa aplicada**.

| Área de foco | Competências |
|---|---|
| **AI Engineering** | Sistemas multi-agente com LangGraph, RAG (Naive, HyDE, Reranking), FastAPI, Next.js, Streamlit, Docker |
| **Avaliação e observabilidade** | RAGAS, BLEU, ROUGE, LLM-as-Judge, LangSmith, Langfuse, OpenTelemetry |
| **Dados e modelagem** | CRISP-DM, scikit-learn, XGBoost, LightGBM, PyTorch, Azure Databricks |
| **Dados e infraestrutura** | PostgreSQL, pgvector, Redis, ChromaDB, Docker Compose, GitHub Actions |

> [!NOTE]
> As páginas detalhadas de cada projeto (em `projects/`) estão escritas em inglês.

---

## Projeto destaque

### [AI Customer Support Platform](projects/ai-customer-support-platform.md) 🎧

<a href="projects/ai-customer-support-platform.md">
  <img src="images/ai-customer-support-platform-with-langgraph/project_cover.png" alt="AI Customer Support Platform" width="900">
</a>

Um **supervisor LangGraph** identifica a intenção de cada ticket e delega para agentes de cobrança, logística ou conta. Esses agentes leem os fatos do pedido no **PostgreSQL**, recuperam procedimentos por **RAG com pgvector** e executam um **motor de políticas determinístico** antes de qualquer reembolso ou cancelamento — de modo que o assistente nunca inventa o estado do pedido nem aprova o que a política proíbe.

São duas interfaces: um Portal do Cliente para o consumidor e um Console de Suporte onde um atendente humano assume o ticket escalado dentro da mesma conversa, com o rastro de ferramentas que o assistente já executou. Publicado na DigitalOcean App Platform, com tracing via OpenTelemetry e Langfuse.

**[Ler o estudo de caso completo →](projects/ai-customer-support-platform.md)** · [Repositório](https://github.com/OtnielGomes/AI-Customer-Support-Platform-With-Langgraph)

---

## Índice de projetos

| Projeto | Problema | Stack | Destaque |
|---|---|---|---|
| [AI Customer Support Platform](projects/ai-customer-support-platform.md) | Responder sobre pedidos reais sem alucinar e escalar quando a política impede agir | LangGraph, FastAPI, Next.js, PostgreSQL/pgvector, Redis | Supervisor multi-agente com políticas determinísticas e human-in-the-loop |
| [AI Agent com Docker](projects/ai-agent-email-docker.md) | Automatizar pesquisa, leitura e envio de e-mails | LangGraph, FastAPI, PostgreSQL, Streamlit, Docker | Publicado na DigitalOcean App Platform |
| [PGD Teletrabalho](projects/pgd-teletrabalho.md) | Responder regras vigentes de teletrabalho a partir do ato em vigor, ou recusar | FastAPI, Next.js, PostgreSQL, Docker | Portão de citação; **89** testes pytest |
| [LLM-Eval-Suite](projects/llm-eval-suite.md) | Comparar LLMs e estratégias de RAG de forma objetiva | Ollama, ChromaDB, RAGAS, LangSmith | RAGAS composto de **0,988** (HyDE, Gemma3 27B) |
| [Previsão de Churn de Cartão](projects/churn-prediction-credit-card.md) | Identificar clientes de cartão com risco de sair | XGBoost, LightGBM, scikit-learn, SHAP | Pipeline CRISP-DM completo com explicabilidade |
| [Classificação de Risco de Crédito](projects/credit-risk-classification.md) | Classificar risco de inadimplência no momento da solicitação | PyTorch, Azure Databricks | **71,08%** de AUC-ROC no teste |
| [Segmentação de Clientes](projects/clustering-segmentation.md) | Descobrir agrupamentos naturais na base de clientes | scikit-learn, CRISP-DM | Em andamento |

---

## AI Engineering

### [AI Agent com Docker Containers e Python](projects/ai-agent-email-docker.md) 🤖

<a href="projects/ai-agent-email-docker.md">
  <img src="images/ai-agent-email/project_cover.png" alt="AI Agent com Docker" width="900">
</a>

Rotinas manuais de e-mail — pesquisar um assunto, ler a caixa de entrada, redigir uma resposta — são lentas e repetitivas. Um **supervisor LangGraph** distribui o trabalho entre agentes de pesquisa e de e-mail, com FastAPI servindo a API, PostgreSQL guardando o histórico de conversas e Streamlit na interface. Empacotado com Docker Compose e publicado na DigitalOcean App Platform.

**[Ver detalhes →](projects/ai-agent-email-docker.md)** · [Repositório](https://github.com/OtnielGomes/AI-Agent-with-Docker-Containers-and-Python)

---

### [PGD Teletrabalho](projects/pgd-teletrabalho.md) 📜

<a href="projects/pgd-teletrabalho.md">
  <img src="images/pgd-teletrabalho/project_cover.png" alt="PGD Teletrabalho" width="900">
</a>

Um servidor da Unifesp que pergunta sobre teletrabalho precisa da regra que está em vigor, com um artigo que dá para abrir. O **Ask** recupera de um recorte datado de cinco atos normativos, redige a resposta e um **portão de citação determinístico** só deixa passar citação cujo artigo foi recuperado. O que o recorte não sustenta volta como **Evidência Insuficiente**. A Resolução CONSU 213/2021 só entra em pergunta histórica.

**89** testes pytest passaram com o rascunho extrativo e a chave de API vazia, incluindo um golden set de **43** itens anotados por uma pessoa. Corte do corpus: **18 de setembro de 2026**.

**[Ver detalhes →](projects/pgd-teletrabalho.md)** · [Repositório](https://github.com/OtnielGomes/Enterprise-Knowledge---RAG-Platform)

---

### [LLM-Eval-Suite](projects/llm-eval-suite.md) 🧪

<a href="projects/llm-eval-suite.md">
  <img src="images/llm-eval/project_cover.png" alt="LLM Eval Suite" width="900">
</a>

Escolher modelo e estratégia de recuperação por intuição não sobrevive a uma revisão. Este benchmark compara estratégias de prompting (Zero-Shot, Few-Shot, CoT) e de RAG (Naive, HyDE, Reranking) entre modelos usando BLEU, ROUGE, LLM-as-Judge e RAGAS, com tracing de ponta a ponta no LangSmith.

Melhor RAGAS composto: **0,988** com HyDE no Gemma3 27B. Melhor acurácia de prompting: média de **89,3%** com Qwen3-Coder 480B.

**[Ver detalhes →](projects/llm-eval-suite.md)** · [Repositório](https://github.com/OtnielGomes/LLM-Eval-Suite)

---

## Ciência de Dados

### [Previsão de Churn de Cartão de Crédito](projects/churn-prediction-credit-card.md) 💳

<a href="projects/churn-prediction-credit-card.md">
  <img src="images/churn-predction/project_cover.png" alt="Previsão de Churn de Cartão de Crédito" width="900">
</a>

Um banco perde receita quando o cliente de cartão sai sem aviso. Pipeline **CRISP-DM** completo — EDA, engenharia de atributos e comparação entre Regressão Logística, SVM, KNN, Random Forest, XGBoost e LightGBM, com divisão estratificada e análise de calibração. Entrega um modelo serializado e uma lista de clientes de alto risco para campanhas de retenção, com SHAP explicando cada previsão.

**[Ver detalhes →](projects/churn-prediction-credit-card.md)** · [Repositório](https://github.com/OtnielGomes/Churn-Prediction-Credit-Card)

---

### [Classificação de Risco de Crédito](projects/credit-risk-classification.md) 💸

<a href="projects/credit-risk-classification.md">
  <img src="images/credit-risk/logoLC.jpeg" alt="Classificação de Risco de Crédito" width="900">
</a>

O risco de inadimplência precisa ser avaliado apenas com o que se sabe antes da aprovação. Uma rede neural em **PyTorch** treinada com dados da LendingClub no **Azure Databricks**, combinada a um classificador de risco em quatro níveis que direciona cada solicitação para aprovação, negação ou reavaliação. **71,08% de AUC-ROC**, 66,42% de acurácia e 63,87% de recall no teste.

**[Ver detalhes →](projects/credit-risk-classification.md)** · [Repositório](https://github.com/OtnielGomes/0_Portfolio-Credit_Risk_Analysis_with_Pytorch)

---

### [Segmentação de Clientes com Clustering](projects/clustering-segmentation.md) 📊

Segmentação não supervisionada para encontrar agrupamentos naturais de clientes — fluxo CRISP-DM com K-Means e clustering hierárquico, avaliados por silhouette score.

> [!NOTE]
> Em andamento — repositório e análise completa em breve.

**[Ver detalhes →](projects/clustering-segmentation.md)**

---

## Sobre este repositório

Este é um **portfólio de demonstração** documentando meu trabalho em **AI Engineering** (foco principal) e **Ciência de Dados** (área complementar de estudo). Cada projeto vive no próprio repositório com o código-fonte completo; aqui ficam os estudos de caso, diagramas de arquitetura, resultados de benchmark e mídias de demonstração que os conectam.

Distribuído sob a licença MIT — veja [`LICENSE`](LICENSE).

## Contato

[![LinkedIn][linkedin-shield]][linkedin-url]
[![GitHub][github-shield]][github-url]

**Otniel Gomes** — AI Engineer

- GitHub: [@OtnielGomes](https://github.com/OtnielGomes)
- LinkedIn: [linkedin.com/in/otnielgomes](https://linkedin.com/in/otnielgomes)

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/otnielgomes

[github-shield]: https://img.shields.io/badge/-GitHub-black.svg?style=for-the-badge&logo=github&colorB=555
[github-url]: https://github.com/OtnielGomes
