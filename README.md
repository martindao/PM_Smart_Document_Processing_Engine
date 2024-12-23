# Smart Document Processing Engine

## Overview
This project powers the document-ingestion and NLP scoring engine for PRDs and assignments. It combines rule-based extraction, MiniLM embeddings, diagnostics, and optimization routines to flag gaps, rank assignments, and produce structured outputs.

## Repository Layout
- pp.py – lightweight API entry point for serving extraction/scoring results.
- main.py – CLI runner used during scheduled experiments.
- models.py – MiniLM embedding wrappers and classifier helper classes.
- optimization.py – heuristics plus reinforcement-style optimizers for assignment scoring.
- utils.py – text cleaning, PDF parsing, and logging helpers.
- data/ – sample PRDs, assignments, and knowledge bases used during tests.
- outputs/ – pipeline logs plus JSON exports that show latest runs.

## Environment Setup
1. Install Python dependencies:
   `powershell
   python -m venv .venv
   .\.venv\Scripts\activate
   pip install -r requirements.txt
   `
2. Set environment variables for model cache locations if you plan to run on air‑gapped machines.

## Running Workflows
- Ad-hoc CLI scoring:
  `powershell
  python main.py --input data/prd_data.json --output outputs/output.json
  `
- API server:
  `powershell
  python app.py
  `
- Review outputs/pipeline.log for the most recent batch runs and diagnostics.

## Quality & Automation
- Run python -m compileall . or uff check . before pushing updates to catch syntax issues.
- Keep data/ entries anonymized—never store proprietary PRDs in the repo.
- When exporting experiment artifacts, place them under outputs/ so future runs can diff results without digging through notebooks.
