---
title: Extração de documentos NFe
slug: nfe-document-extraction
locale: pt
context: Projeto de portfólio
timeline: "2025 — 2026"
focusArea: Inferência validada e IA documental
repository: https://github.com/OtnielGomes/NFe-Document-Extraction
imageDir: nfe-document-extraction
tech:
  - Python
  - LangGraph
  - OpenAI
  - LangSmith
  - Docker
---

# Extração de documentos NFe

| | |
|---|---|
| **Contexto** | Projeto de portfólio |
| **Linha do tempo** | 2025 — 2026 |
| **Foco** | Inferência validada e IA documental |

Python · LangGraph · OpenAI · LangSmith · Docker

## Visão geral

Escritórios e pequenos negócios ainda digitam ou conferem notas fiscais manualmente. A DANFE chega em PDF digital ou foto de celular; chave de acesso, CNPJ, itens e totais precisam virar JSON estruturado. Um LLM que “lê a página” não é fonte da verdade—um dígito errado no CNPJ ou um total que não fecha tem que ser barrado antes de lançar no ERP.

Agentes de cabeçalho e de itens extraem os campos. Um **validador determinístico** só aceita valor quando dígitos verificadores, consistência da chave, aritmética das linhas, totais e formatos passam. Há **uma única tentativa de correção**, reenviando só os campos que falharam com as mensagens do validador. O que ainda falhar vai para **revisão humana**, com esses campos sinalizados. Novas tentativas em loop são proibidas de propósito: modelo que vai ajustando número até fechar a conta está inventando dado que só passa no teste.

Em PDF digital, a configuração adotada atinge **0,9870** de acurácia por campo a **US$ 0,002035** por nota (visão barata, `gpt-6-luna`), com detecção de erro plantado em **1,0000**. Experimentos e traces ficam no LangSmith; checagens de qualidade rodam sem chamar modelo.

**Repositório:** [NFe-Document-Extraction](https://github.com/OtnielGomes/NFe-Document-Extraction)

## Arquitetura

Extração, validação, uma correção e revisão humana—sem retentativas ilimitadas no modelo.

![Diagrama de arquitetura](../../architecture-cases/nfe-document-extraction-pt.png)

## Passo a passo da implementação

### FASE 01 — Entrada e tipo de mídia

O pipeline aceita DANFE em PDF e fotos simuladas. Visão ou camada de texto alimentam os mesmos agentes orientados a schema, conforme o tipo de documento.

### FASE 02 — Extração multiagente

Agentes separados preenchem cabeçalho e itens. A saída é provisória até o validador rodar.

### FASE 03 — Validação determinística

Regras em Python cobrem CNPJ, chave NFe, matemática por linha, totais e formatos. Falhas trazem motivo estruturado para a etapa de correção.

### FASE 04 — Uma passagem de correção

Um único reprocessamento manda de volta só os campos com erro e o feedback do validador. Segunda falha encerra automação e aciona **revisão humana**—por desenho.

### FASE 05 — Avaliação e observabilidade

Experimentos no LangSmith compararam modelos e mídias; métricas (acurácia por campo, custo por nota, taxa de revisão) escolheram a configuração em produção. UI local em PT/EN e feedback de visitante quando há chave configurada.

## Stack em detalhe

### LangGraph

Orquestra extração e correção como passos explícitos no grafo, em vez de loops soltos no código.

### Validador determinístico (Python)

A verdade de negócio fica fora do modelo—o núcleo de “o modelo lê; o código decide se confia”.

### OpenAI visão / Responses API

Visão barata cobre foto onde a camada de texto não chega; o modelo foi medido, não assumido.

### LangSmith

Traces, datasets e tabelas de experimento tornam acurácia e custo auditáveis.

### Docker

Superfície reproduzível para API e interface de demo.
