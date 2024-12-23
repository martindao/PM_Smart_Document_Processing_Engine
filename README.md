# Smart Document Processing Engine

## Overview
This project powers the document-ingestion and NLP scoring engine for PRDs and assignments. It combines rule-based extraction, MiniLM embeddings, diagnostics, and optimization routines to flag gaps, rank assignments, and produce structured outputs.

## Repository Layout
- pp.py – lightweight FastAPI/Flask entry point for serving extraction/scoring results.
- main.py – CLI runner used during scheduled experiments.
- models.py – MiniLM embedding wrappers and classifier helper classes.
- optimization.py – heuristics + reinforcement-style optimizers for assignment scoring.
- utils.py – text cleaning, PDF parsing, and logging helpers.
- data/ – sample PRDs, assignments, and knowledge bases used during tests.
- outputs/ – pipeline logs plus JSON exports that show latest runs.

## Environment Setup
1. Install Python dependencies:
   `powershell
   python -m venv .venv
   .\.venv\Scripts\activate
   pip install -r requirements.txt  # create from pip freeze if missing
   `
2. Set environment variables for model cache locations if you plan to run on air-gapped machines.

## Running Workflows
- Ad-hoc CLI scoring:
  `powershell
  python main.py --input data/prd_data.json --output outputs/output.json
  `
- API server (for integration tests):
  `powershell
  python app.py
  `
- Notebook-style experiments live as Markdown logs; reference outputs/pipeline.log for the most recent batch runs.

## Quality & Automation
- Run python -m compileall . or uff check . before committing to catch syntax errors.
- Keep data/ entries anonymized—never commit proprietary PRDs.
- Align commit timestamps with the 2022–2024 activity window defined in OpenSpec (final commit on 2024-10-25).
