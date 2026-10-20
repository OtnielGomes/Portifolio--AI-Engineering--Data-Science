<a id="top"></a>

[← Voltar ao portfólio](../README.pt-BR.md)

**Idioma:** [English](credit-risk-classification.md) | Português

# Classificação de risco de crédito 💸

[![PyTorch](https://img.shields.io/badge/PyTorch-neural%20nets-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Azure](https://img.shields.io/badge/Azure-Databricks-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)](https://azure.microsoft.com/)

**Repositório:** [0_Portfolio-Credit_Risk_Analysis_with_Pytorch](https://github.com/OtnielGomes/0_Portfolio-Credit_Risk_Analysis_with_Pytorch)

<div align="center">
  <a href="https://github.com/OtnielGomes/0_Portfolio-Credit_Risk_Analysis_with_Pytorch">
    <img src="covers/credit-risk-classification/cover.pt.png" alt="credit-risk-classification cover" width="900">
  </a>
</div>

| | |
|---|---|
| **Contexto** | Projeto de portfólio |
| **Linha do tempo** | 2024 — 2025 |
| **Foco** | ML tabular e score de risco |

PyTorch · Azure Databricks · LendingClub

## Visão geral

Instituições precisam estimar risco de inadimplência no momento da proposta, só com informação disponível antes da aprovação. Aprovar demais corrói margem; negar em excesso deixa receita na mesa.

Uma **rede neural PyTorch** treina em empréstimos LendingClub no **Azure Databricks**. Um **classificador em quatro níveis** mapeia o score do modelo para faixas de risco muito baixo, baixo, médio e muito alto, orientando aprovação, análise condicional ou rejeição automática com significado de negócio explícito por faixa.

No conjunto de teste o modelo atinge **71,08% de AUC-ROC**, **66,42% de acurácia** e **63,87% de recall**—com matriz de confusão e gráficos de score no repositório para auditoria.


## Arquitetura

Das features de empréstimo ao score neural e às faixas de risco operacionais.

![Diagrama de arquitetura](architecture-cases/credit-risk-classification-pt.png)

## Passo a passo da implementação

### FASE 01 — Dados e contexto de features

Empréstimos históricos LendingClub trazem label (default vs quitado) e atributos pré-aprovação. Exploração no Databricks define quais sinais entram na rede.

### FASE 02 — Treino da rede neural

PyTorch define arquitetura feed-forward, função de perda e loop de treino na matriz preparada. Treino e validação rodam no workspace Databricks.

### FASE 03 — Avaliação no teste

Métricas incluem AUC-ROC, acurácia, F1 e recall em hold-out. Matriz de confusão e visualizações de score documentam comportamento por classe—nota única não basta.

### FASE 04 — Taxonomia de quatro níveis

Regras pós-modelo traduzem risco contínuo em faixas **muito baixo**, **baixo**, **médio** e **muito alto**, com descrição operacional (taxa, aprovação condicional, rejeição automática).

### FASE 05 — Saída interpretável

Exemplos de resposta do classificador combinam probabilidade de default com checagens por feature (DTI, sub-grade etc.) para o analista ver *por que* a faixa foi atribuída.

## Stack em detalhe

### PyTorch

Treino flexível em features tabulares de crédito quando baselines sklearn ficam curtos, sem complexidade de deep learning em produção.

### Azure Databricks

Ambiente Spark/Python gerenciado para notebooks reproduzíveis e volume de dados em escala de portfólio acadêmico.

### Classificador em quatro níveis

Ponte entre score bruto e linguagem de política de crédito que risco e recrutamento reconhecem.

### Dataset LendingClub

Benchmark público de default—limitações (viés de época, survivorship) entram na narrativa honesta de ciência de dados.

## Níveis de classificação de risco

| Risk level | Description |
|---|---|
| **Very low risk** | High repayment probability, eligible for lower rates |
| **Low risk** | Likely repaid, requires careful evaluation |
| **Medium risk** | Conditional approval or justified denial |
| **Very high risk** | Strong default probability — automatic rejection |

> [!NOTE]
> Per-class accuracy values in the original analysis should be verified against the [source repository](https://github.com/OtnielGomes/0_Portfolio-Credit_Risk_Analysis_with_Pytorch) — some class-level metrics share identical values and may reflect grouping rather than distinct scores.

## Test data metrics

| Metric | Value |
|---|---|
| **AUC-ROC** | 71.08% |
| **Accuracy** | 66.42% |
| **F1 Score** | 37.41% |
| **Recall** | 63.87% |

<div align="left">
  <img src="../images/credit-risk/scores_models.png" alt="Model scores on validation data" width="900">
</div>

<div align="left">
  <img src="../images/credit-risk/test_matrix.png" alt="Confusion matrix on test data" width="300">
</div>

<details>
<summary>View example classifier output</summary>

```text
This loan has a: 46.75% chance of defaulting
Loan approved! --- Very low default risk loan

This loan has been deemed very low risk because some of the scores below meet the criteria required for loan approval.

expen_cr_inc: D >>>> Not OK
score_cr: 716.67 >>>> OK
ability_to_pay: 11.26 >>>> Not OK
dti: 27.65 >>>> Not OK

### sub_grade ###: B2 >>>> OK
```

</details>

<p align="right">(<a href="#top">voltar ao topo</a>)</p>
