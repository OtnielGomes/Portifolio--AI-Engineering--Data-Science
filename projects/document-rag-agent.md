<a id="top"></a>

[← Back to portfolio](../README.md)

# Document RAG Agent 🗂️

[![LangChain](https://img.shields.io/badge/LangChain-RAG-1C3C3C?style=flat-square)](https://www.langchain.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-embeddings-F97316?style=flat-square)](https://www.trychroma.com/)

**Repository:** [Document-Rag-Agent](https://github.com/OtnielGomes/Document-Rag-Agent)

<div align="center">
  <a href="https://github.com/OtnielGomes/Document-Rag-Agent">
    <img src="../images/document_rag_agent/project_cover.png" alt="Document RAG Agent project cover" width="900">
  </a>
</div>

**Problem:** Finding accurate answers inside long PDF documents is slow when relying on manual search or unconstrained LLM responses.

**Solution:** A **RAG-based Q&A system** with PDF ingestion, text chunking, semantic search via **ChromaDB**, and context-aware generation through **LangChain** and **Streamlit**, with prompt rules to reduce hallucinations.

**Result:** Grounded answers from uploaded PDFs (tested with a resume as knowledge base), with manual evaluation of accuracy and application latency.

## Architecture

| Stage | Technology | Purpose |
|---|---|---|
| Ingestion | PyMuPDF | Extract text from PDF uploads |
| Chunking & embedding | LangChain, ChromaDB | Split documents and store vectors |
| Generation | LLM via LangChain | Context-aware answer synthesis |
| Interface | Streamlit | Upload, query, and review metrics |

## Demo

[![Demonstration video](../images/document_rag_agent/video.png)](https://canva.link/zjmai0hdpe9v8lf)

<details>
<summary>View application screenshots</summary>

### Loading PDF

<img src="../images/document_rag_agent/pdf1.png" alt="Loading PDF" width="500">

### Asking the agent

<img src="../images/document_rag_agent/question7.png" alt="Asking the agent" width="700">

### Latency and metrics

<img src="../images/document_rag_agent/metrics.png" alt="Application metrics" width="700">

</details>

<p align="right">(<a href="#top">back to top</a>)</p>
