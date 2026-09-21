<a id="top"></a>

[← Back to portfolio](../README.md)

# LLM-Eval-Suite 🧪

[![Ollama](https://img.shields.io/badge/Ollama-inference-000000?style=flat-square)](https://ollama.com/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-vector%20store-F97316?style=flat-square)](https://www.trychroma.com/)
[![RAGAS](https://img.shields.io/badge/RAGAS-evaluation-6366F1?style=flat-square)](https://docs.ragas.io/)
[![LangSmith](https://img.shields.io/badge/LangSmith-tracing-FF6B35?style=flat-square)](https://smith.langchain.com/)

**Repository:** [LLM-Eval-Suite](https://github.com/OtnielGomes/LLM-Eval-Suite)

<div align="center">
  <a href="https://github.com/OtnielGomes/LLM-Eval-Suite">
    <img src="../images/llm-eval/project_cover.png" alt="LLM Eval Suite project cover" width="900">
  </a>
</div>

**Problem:** Choosing the right LLM and RAG strategy requires systematic comparison — ad-hoc testing is not reproducible or measurable.

**Solution:** A benchmark framework comparing **prompting strategies** (Zero-Shot, Few-Shot, CoT) and **RAG retrieval strategies** (Naive, HyDE, Reranking) with BLEU, ROUGE, LLM-as-Judge, and RAGAS — all traced via **LangSmith**.

**Result:** **0.988** composite RAGAS score with HyDE on Gemma3 27B; **89.3%** mean accuracy with Qwen3-Coder 480B across prompting strategies.

## Architecture

| Component | Backend | Model | Purpose |
|---|---|---|---|
| Generation | Ollama Cloud | Configurable via `.env` | Answer generation |
| Embeddings | Ollama Local | `nomic-embed-text` | Document & query embeddings |
| Judge | Ollama Cloud | Configurable via `.env` | LLM-as-Judge scoring |
| Vector Store | Local | ChromaDB | Document retrieval |

## Results — Prompting accuracy

![Accuracy per Strategy × Model](../images/llm-eval/benchmark_accuracy_grouped.png)

| Model | Zero-Shot | Few-Shot | CoT | Mean |
|---|---|---|---|---|
| **Qwen3-Coder 480B** | 90% | 88% | 90% | **89.3%** |
| Gemma3 27B | 68% | 64% | 88% | 73.3% |
| GPT-OSS 20B | 0% | 4% | 8% | 4% |

## Results — RAG composite RAGAS score

![Composite RAGAS Score per Strategy × Model](../images/llm-eval/rag_composite_grouped.png)

| Model | Naive | HyDE | Reranking | Mean |
|---|---|---|---|---|
| **Gemma3 27B** | 0.968 | **0.988** | 0.969 | **0.975** |
| Qwen3-Coder 480B | 0.971 | 0.973 | 0.922 | 0.955 |
| GPT-OSS 20B | 0.651 | 0.000 | 0.653 | 0.435 |

## Results — Latency

![Benchmark latency](../images/llm-eval/benchmark_latency.png)

<details>
<summary>View detailed benchmark charts</summary>

![Accuracy heatmap](../images/llm-eval/benchmark_accuracy_heatmap.png)

![ROUGE-L heatmap](../images/llm-eval/benchmark_rougeL_heatmap.png)

![LLM-as-Judge heatmap](../images/llm-eval/benchmark_judge_heatmap.png)

![RAG composite heatmap](../images/llm-eval/rag_composite_heatmap.png)

![RAG heatmaps overview](../images/llm-eval/rag_heatmaps.png)

![RAG radar per model](../images/llm-eval/rag_radar_per_model.png)

![RAG recall distribution](../images/llm-eval/rag_recall_dist.png)

</details>

<p align="right">(<a href="#top">back to top</a>)</p>
