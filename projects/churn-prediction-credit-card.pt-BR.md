<a id="top"></a>

[← Voltar ao portfólio](../README.pt-BR.md)

**Idioma:** [English](churn-prediction-credit-card.md) | Português

# Previsão de churn de cartão de crédito 💳

[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-boosting-01BFFF?style=flat-square)](https://xgboost.ai/)
[![LightGBM](https://img.shields.io/badge/LightGBM-boosting-0078D4?style=flat-square)](https://lightgbm.readthedocs.io/)

**Repositório:** [Churn-Prediction-Credit-Card](https://github.com/OtnielGomes/Churn-Prediction-Credit-Card)

<div align="center">
  <a href="https://github.com/OtnielGomes/Churn-Prediction-Credit-Card">
    <img src="covers/churn-prediction-credit-card/cover.pt.png" alt="churn-prediction-credit-card cover" width="900">
  </a>
</div>

| | |
|---|---|
| **Contexto** | Projeto de portfólio |
| **Linha do tempo** | 2024 — 2025 |
| **Foco** | CRISP-DM e ML tabular explicável |

scikit-learn · XGBoost · LightGBM · SHAP

## Visão geral

O banco perde receita quando clientes de cartão cancelam sem alerta antecipado. Marketing precisa de uma lista ranqueada de risco—nota de caixa-preta que compliance e negócio não aceitam.

Um pipeline **CRISP-DM** de ponta a ponta cobre entendimento do negócio, EDA, engenharia de features e comparação de Regressão Logística, SVM, KNN, Random Forest, **XGBoost** e **LightGBM**, com divisão estratificada e análise de calibração. O artefato final é modelo serializado (`joblib`) e explicações SHAP do porquê de um cliente estar em alto risco.

Entregável: **lista de clientes de alto risco** para campanhas de retenção, com metodologia e gráficos no repositório.


## Arquitetura

Dos KPIs de negócio ao modelo e à pontuação em lote para uso tipo CRM.

![Diagrama de arquitetura](architecture-cases/churn-prediction-credit-card-pt.png)

## Passo a passo da implementação

### FASE 01 — Entendimento do negócio

Target binário de churn, lift de campanha como métrica de sucesso e definição clara de cancelamento na janela do dataset.

### FASE 02 — Entendimento e preparação dos dados

EDA de desbalanceamento, correlação e qui-quadrado, padronização z-score, one-hot e split estratificado preservando proporção de classes.

### FASE 03 — Comparação de modelos

Treino e comparação de modelos clássicos e boosting na validação—AUC-ROC, F1, recall—com curvas de calibração, não só acurácia.

### FASE 04 — Explicabilidade e escolha

SHAP destaca drivers da probabilidade de churn no modelo escolhido, apoiando seleção e narrativa para marketing.

### FASE 05 — Artefato de deploy

Exportação em `joblib` e caminho de scoring em lote que gera a lista priorizada (screenshots de deploy documentados no repo).

## Stack em detalhe

### Estrutura CRISP-DM

Mostra capacidade de conduzir projeto analítico completo, não só um algoritmo.

### XGBoost / LightGBM

Baselines fortes em features tabulares “de banco”, com treino eficiente em target desbalanceado.

### Ecossistema scikit-learn

Modelos lineares e por distância dão âncora interpretável frente aos boosters.

### SHAP

Liga score a contribuição por feature—esperado em contextos próximos a banco e compliance.

### Artefato joblib

Padrão prático de handoff do notebook para algo que o CRM poderia agendar, mesmo como simulação de portfólio.

## CRISP-DM methodology

| **Stage** | **Objective** | **Methodological execution** |
| :--- | :--- | :--- |
| **1. Business Understanding** | Mitigate revenue loss by identifying at-risk customers. | • **Target definition**: Binary classification (Churn: Yes/No).<br>• **KPIs**: Maximize **Lift** in retention campaigns & revenue saved vs. cost. |
| **2. Data Understanding** | Detect patterns of friction and dissatisfaction. | • **EDA**: Distribution analysis (detect imbalance).<br>• **Hypothesis testing**: Correlation matrix & independence tests (Chi-Square). |
| **3. Data Preparation** | Construct a robust dataset for parametric modeling. | • **Scaling**: Standardization (Z-score).<br>• **Encoding**: One-Hot Encoding.<br>• **Splitting**: Stratified train/test split. |
| **4. Modeling** | Estimate churn probability. | • **Algorithms**: Logistic Regression, SVM LinearSVC, KNN, Random Forest, XGBoost, LightGBM. |
| **5. Evaluation** | Assess model reliability and financial impact. | • **Metrics**: AUC-ROC, F1-Score, Recall, calibration curve. |
| **6. Deployment** | Integrate insights into the CRM lifecycle. | • **Deliverable**: High-risk customer list for the marketing squad.<br>• **Artifact**: Serialized model (`joblib`) for batch inference. |

## Final model — test data

<div align="center">
  <img src="../images/churn-predction/evaluation.png" alt="Final model evaluation" width="500">
</div>

<details>
<summary>View EDA, model comparison, and explainability</summary>

### Numerical & categorical variables

<img src="../images/churn-predction/hist_bi.png" alt="Histograms" width="900">
<br />
<img src="../images/churn-predction/count_bi.png" alt="Count plots" width="900">

### Churn rate — training data

<div align="center">
  <img src="../images/churn-predction/target_count.png" alt="Target count" width="900">
</div>

### Model scores on validation data

<img src="../images/churn-predction/scores_models.png" alt="Model scores" width="900">

### Probability distribution & SHAP

<img src="../images/churn-predction/probabilities.png" alt="Probabilities" width="900">
<br />
<img src="../images/churn-predction/shap_val_1.png" alt="SHAP values" width="900">
<br />
<img src="../images/churn-predction/shap_val.png" alt="SHAP summary" width="900">

### Correlation analysis

<img src="../images/churn-predction/corr_bi.png" alt="Correlation matrix" width="900">

### Deployment artifacts

<img src="../images/churn-predction/function_deploy.png" alt="Deployment function" width="900">
<br />
<img src="../images/churn-predction/output_deploy.png" alt="Deployment output" width="900">

</details>

<p align="right">(<a href="#top">voltar ao topo</a>)</p>
