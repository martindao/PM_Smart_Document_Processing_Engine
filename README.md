# Smart Document Processing Engine

## Overview
This project powers the document-ingestion and NLP scoring engine for PRDs and assignments. It combines rule-based extraction, MiniLM embeddings, diagnostics, and optimization routines to flag gaps, rank assignments, and produce structured outputs.

## What This Repo Is
A supporting PM-workflow document processing engine. It provides:
- Document ingestion and parsing for PRDs and assignment documents
- NLP-based scoring and gap detection using MiniLM embeddings
- CLI and lightweight API interfaces for batch and ad-hoc processing
- Structured JSON outputs for downstream analysis

This repo exists as a standalone supporting track, separate from the core Support/QA/DE wedge.

## What This Repo Is NOT
This project does NOT provide:
- Zendesk, Jira, or Slack integrations
- Playwright, Cypress, or Selenium browser automation
- Airflow, Snowflake, or dbt data platform proof

Those capabilities belong in other dedicated repositories.

## Sample Document-Processing Workflow
The engine offers two primary interfaces:

**CLI (main.py):**
```powershell
python main.py --input data/prd_data.json --output outputs/output.json
```
This runs batch scoring on input documents and writes structured results to the output file.

**Streamlit Interface (app.py):**
```powershell
python app.py
```
Launches a lightweight web interface for interactive document processing and result review.

After running either workflow, check `outputs/pipeline.log` for diagnostics and batch run details.

## Repository Layout
- `app.py` – lightweight API entry point for serving extraction/scoring results.
- `main.py` – CLI runner used during scheduled experiments.
- `models.py` – MiniLM embedding wrappers and classifier helper classes.
- `optimization.py` – heuristics plus reinforcement-style optimizers for assignment scoring.
- `utils.py` – text cleaning, PDF parsing, and logging helpers.
- `data/` – sample PRDs, assignments, and knowledge bases used during tests.
- `outputs/` – pipeline logs plus JSON exports that show latest runs.

## Environment Setup
1. Install Python dependencies:
```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

2. Set environment variables for model cache locations if you plan to run on air-gapped machines.

## Running Workflows
- Ad-hoc CLI scoring:
```powershell
python main.py --input data/prd_data.json --output outputs/output.json
```

- API server:
```powershell
python app.py
```

- Review `outputs/pipeline.log` for the most recent batch runs and diagnostics.

## Quality & Automation
- Run `python -m compileall .` or `ruff check .` before pushing updates to catch syntax issues.
- Keep `data/` entries anonymized—never store proprietary PRDs in the repo.
- When exporting experiment artifacts, place them under `outputs/` so future runs can diff results without digging through notebooks.
