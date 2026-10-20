---
title: Credit Risk Classification
slug: credit-risk-classification
locale: en
context: Independent portfolio
timeline: "2024 — 2025"
focusArea: Tabular ML & risk scoring
repository: https://github.com/OtnielGomes/0_Portfolio-Credit_Risk_Analysis_with_Pytorch
imageDir: credit-risk
tech:
  - PyTorch
  - Azure Databricks
  - LendingClub data
---

# Credit Risk Classification

| | |
|---|---|
| **Context** | Independent portfolio |
| **Timeline** | 2024 — 2025 |
| **Focus area** | Tabular ML & risk scoring |

PyTorch · Azure Databricks · LendingClub

## Overview

Lenders must estimate default risk at application time using only information available before approval. Wrong approvals erode margin; overly conservative denials leave revenue on the table.

A **PyTorch neural network** trains on LendingClub loan data inside **Azure Databricks**. A **four-level risk classifier** maps model scores to very low, low, medium, and very high risk bands, routing each application toward approval, conditional review, or automatic rejection with explicit business meaning per band.

On held-out test data the model reaches **71.08% AUC-ROC**, **66.42% accuracy**, and **63.87% recall**—reported with confusion-matrix and score plots in the repository for audit.

**Repository:** [0_Portfolio-Credit_Risk_Analysis_with_Pytorch](https://github.com/OtnielGomes/0_Portfolio-Credit_Risk_Analysis_with_Pytorch)

## Architecture

From raw loan features through neural scoring to policy-style risk levels.

![Architecture diagram](../../architecture-cases/credit-risk-classification-en.png)

## Implementation walkthrough

### PHASE 01 — Data sourcing and feature context

LendingClub historical loans supply labels (default vs paid) and pre-approval attributes. Exploratory work in Databricks frames which signals feed the network.

### PHASE 02 — Neural model training

PyTorch defines the feed-forward architecture, loss, and training loop on the prepared feature matrix. Training and validation run in the Databricks workspace for scalable compute.

### PHASE 03 — Evaluation on test split

Metrics include AUC-ROC, accuracy, F1, and recall on a held-out test set. Confusion matrix and score visualizations document class behavior—not just a single headline number.

### PHASE 04 — Four-level risk taxonomy

Post-model rules translate continuous risk into **very low**, **low**, **medium**, and **very high** bands with operational descriptions (rate eligibility, conditional approval, automatic reject).

### PHASE 05 — Interpretable decision output

Example classifier responses combine default probability with per-feature checks (e.g. debt-to-income, sub-grade) so a human underwriter sees *why* a band was assigned.

## Tech stack deep-dive

### PyTorch

Flexible training for tabular credit features when you outgrow sklearn baselines but stay below production deep-learning complexity.

### Azure Databricks

Managed Spark/Python environment for repeatable notebooks, data volume, and team-style ML workflows on academic portfolio scale.

### Four-level classifier

Bridges raw model scores to credit-policy language recruiters and risk teams recognize.

### LendingClub dataset

Public, well-understood benchmark for default prediction—limitations (survivorship, era) are part of honest data-science storytelling.
