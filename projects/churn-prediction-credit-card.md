<a id="top"></a>

[← Back to portfolio](../README.md)

**Language:** English | [Português](churn-prediction-credit-card.pt-BR.md)

# Credit Card Churn Prediction 💳

[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-boosting-01BFFF?style=flat-square)](https://xgboost.ai/)
[![LightGBM](https://img.shields.io/badge/LightGBM-boosting-0078D4?style=flat-square)](https://lightgbm.readthedocs.io/)

**Repository:** [Churn-Prediction-Credit-Card](https://github.com/OtnielGomes/Churn-Prediction-Credit-Card)

<div align="center">
  <a href="https://github.com/OtnielGomes/Churn-Prediction-Credit-Card">
    <img src="covers/churn-prediction-credit-card/cover.en.png" alt="churn-prediction-credit-card cover" width="900">
  </a>
</div>

| | |
|---|---|
| **Context** | Independent portfolio |
| **Timeline** | 2024 — 2025 |
| **Focus area** | CRISP-DM & explainable tabular ML |

scikit-learn · XGBoost · LightGBM · SHAP

## Overview

A bank loses revenue when credit-card customers churn without early warning. Marketing needs a ranked list of at-risk cardholders—not a black box that cannot be defended to compliance or the business.

An end-to-end **CRISP-DM** pipeline covers business framing, EDA, feature engineering, and comparison of Logistic Regression, SVM, KNN, Random Forest, **XGBoost**, and **LightGBM** with stratified splits and calibration analysis. The final artifact is a serialized model (`joblib`) plus SHAP explanations for why a customer scored high risk.

Deliverable: a **high-risk customer list** for targeted retention campaigns, with methodology and plots documented in the repository.


## Architecture

From business KPIs through modeling to batch scoring for CRM-style use.

![Architecture diagram](architecture-cases/churn-prediction-credit-card-en.png)

## Implementation walkthrough

### PHASE 01 — Business understanding

Binary churn target, campaign lift as the success lens, and clear definition of what “churn” means in the dataset window.

### PHASE 02 — Data understanding & preparation

EDA on imbalance, correlation and chi-square tests, z-score scaling, one-hot encoding, and stratified train/test split to preserve class ratios.

### PHASE 03 — Model comparison

Train and compare classical and boosting models on validation metrics—AUC-ROC, F1, recall—and inspect calibration curves, not accuracy alone.

### PHASE 04 — Explainability & selection

SHAP values highlight drivers of churn probability for the chosen model, supporting both model selection and marketing narrative.

### PHASE 05 — Deployment artifact

Export `joblib` model and batch-scoring path that outputs the prioritized retention list (documented deployment screenshots in the repo).

## Tech stack deep-dive

### CRISP-DM structure

Shows you can run a full analytics project, not only fit one algorithm.

### XGBoost / LightGBM

Strong baselines on tabular bank-like features with efficient training on imbalanced targets.

### scikit-learn ecosystem

Linear and distance models provide interpretable anchors against complex boosters.

### SHAP

Connects model scores to per-feature contributions—expected in regulated-adjacent retail banking contexts.

### joblib artifact

Practical handoff pattern from notebook to “something CRM could schedule,” even as a portfolio simulation.

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

<p align="right">(<a href="#top">back to top</a>)</p>
