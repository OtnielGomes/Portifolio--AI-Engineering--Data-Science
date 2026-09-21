<a id="top"></a>

[← Back to portfolio](../README.md)

# Credit Card Churn Prediction 💳

[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-boosting-01BFFF?style=flat-square)](https://xgboost.ai/)
[![LightGBM](https://img.shields.io/badge/LightGBM-boosting-0078D4?style=flat-square)](https://lightgbm.readthedocs.io/)

**Repository:** [Churn-Prediction-Credit-Card](https://github.com/OtnielGomes/Churn-Prediction-Credit-Card)

<div align="center">
  <a href="https://github.com/OtnielGomes/Churn-Prediction-Credit-Card">
    <img src="../images/churn-predction/project_cover.png" alt="Churn Prediction project cover" width="900">
  </a>
</div>

**Problem:** A banking institution loses revenue when credit-card customers churn without early warning.

**Solution:** End-to-end **CRISP-DM** pipeline — EDA, feature engineering, and comparison of Logistic Regression, SVM, KNN, Random Forest, XGBoost, and LightGBM with stratified splits and calibration analysis.

**Result:** Production-ready artifact (`joblib`) delivering a high-risk customer list for targeted retention campaigns, with SHAP-based explainability.

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
