# Portfolio Positioning

This document defines the scope and positioning of the Smart Document Processing Engine within the broader portfolio context.

## Portfolio Positioning

This project is a **supporting-track PM-workflow project**. It demonstrates document processing and NLP-based routing capabilities, but it is not part of the primary portfolio wedge.

The main portfolio wedge consists of:
- **Support tooling**: Zendesk, Jira, Slack integrations
- **QA automation**: Playwright, Cypress, Selenium frameworks
- **Data engineering platform**: Airflow, Snowflake, dbt pipelines

This project operates in a separate supporting lane and does not compete with or claim to strengthen that primary wedge.

---

### What This Project Strengthens

This project provides evidence for:

- **Document ingestion and NLP scoring workflow proof**: Demonstrates a working pipeline for parsing requirements documents and scoring them for priority/routing decisions.

- **MiniLM embedding usage for semantic similarity**: Shows practical application of sentence-transformers embeddings for document similarity and classification tasks.

- **Multi-mode pipeline demonstration**: Implements basic, advanced, and optimized processing modes to show progressive refinement in document handling workflows.

These elements support a PM-focused narrative around requirements parsing, document triage, and workflow automation.

---

### What This Project Does NOT Strengthen

This project does not provide evidence for:

- **Support tooling**: No Zendesk, Jira, Slack, or ticketing system integrations. This is not a support operations project.

- **QA automation**: No Playwright, Cypress, Selenium, or browser testing frameworks. This is not a QA automation project.

- **Data engineering platform**: No Airflow orchestration, Snowflake warehousing, or dbt transformation pipelines. This is not a data engineering platform project.

---

## Non-Duplication Statement

This project is a **separate supporting track** and does not compete with the primary Support + QA + Data Engineering portfolio wedge.

Recruiters and reviewers should evaluate this project as:
- A PM-workflow demonstration project
- A focused NLP/document-processing proof point
- Supplementary evidence, not core portfolio positioning

The primary portfolio story lives elsewhere. This project supports that story from a distance, not as a central pillar.

---

## Claim-Evidence Matrix

This section maps every portfolio claim to its exact repository evidence. All claims are verified against source files.

### Core Capability Claims

| Claim | Source Surface | Evidence Path | Verification |
|-------|----------------|---------------|--------------|
| Document parsing and extraction from PRDs | README.md (L8), landing/index.html (L114), demo/index.html (L296) | `main.py` L18-21: `PRDIngestionJSON(args.prd_file).load_prd()`; `app.py` L13-18: file upload and JSON parsing | ✓ verified |
| NLP-based scoring using MiniLM embeddings | README.md (L4, L9), architecture-overview.md (L70), landing/index.html (L118), demo/index.html (L317) | `outputs/pipeline.log` L2: `Load pretrained SentenceTransformer: all-MiniLM-L6-v2` (repeated L10, L12, L36, etc.) | ✓ verified |
| CLI interface for batch processing | README.md (L10, L26-30), architecture-overview.md (L99) | `main.py` L1-47: argparse CLI with `--mode`, `--prd_file`, `--engineers` arguments | ✓ verified |
| Streamlit interface for interactive processing | README.md (L10, L32-36), architecture-overview.md (L100) | `app.py` L1-80: Streamlit web interface with file upload, mode selection, and download buttons | ✓ verified |
| Structured JSON outputs (epics, user stories, assignments) | README.md (L11), landing/index.html (L126), sample-workflow.md (L92-96) | `outputs/output.json` L1-36: contains `epics`, `user_stories`, `assignments` arrays | ✓ verified |
| Multi-mode pipeline (basic, advanced, optimized) | architecture-overview.md (L67-71), sample-workflow.md (L66) | `main.py` L11-12, L23-28: mode selection; `app.py` L21-32: mode selectbox | ✓ verified |
| Knapsack optimization for workload balancing | architecture-overview.md (L71, L88) | `main.py` L33-35: `optimize_workload_knapsack()` call; `outputs/pipeline.log` L28: `Optimized Assignments (Knapsack DP)` | ✓ verified |

### Positioning Claims

| Claim | Source Surface | Evidence Path | Verification |
|-------|----------------|---------------|--------------|
| Supporting PM-workflow document processing engine | README.md (L7, L13), portfolio-positioning.md (L7), landing/index.html (L96, L103), demo/index.html (L201) | Consistent across all surfaces | ✓ verified |
| Standalone supporting track, separate from core Support/QA/DE wedge | README.md (L13), portfolio-positioning.md (L14, L46), landing/index.html (L103) | Consistent across all surfaces | ✓ verified |
| No Zendesk, Jira, or Slack integrations | README.md (L17), portfolio-positioning.md (L36), landing/index.html (L139) | Consistent across all surfaces | ✓ verified |
| No Playwright, Cypress, or Selenium browser automation | README.md (L18), portfolio-positioning.md (L39), landing/index.html (L143) | Consistent across all surfaces | ✓ verified |
| No Airflow, Snowflake, or dbt data platform | README.md (L19), portfolio-positioning.md (L40), landing/index.html (L147) | Consistent across all surfaces | ✓ verified |

### Cross-Surface Harmonization Status

All surfaces have been verified for consistency:

| Surface | Positioning Statement | Status |
|---------|----------------------|--------|
| README.md | "A supporting PM-workflow document processing engine" (L7) | ✓ consistent |
| architecture-overview.md | "transforms PRD documents and engineer profiles into structured task assignments" (L5) | ✓ consistent |
| sample-workflow.md | "Smart Document Processing Engine pipeline" (L3) | ✓ consistent |
| portfolio-positioning.md | "supporting-track PM-workflow project" (L7) | ✓ consistent |
| landing/index.html | "supporting PM-workflow document processing engine" (L96) | ✓ consistent |
| demo/index.html | "Supporting PM-workflow document processor" (L201) | ✓ consistent |

### Wedge-Boundary Statement

The following statement appears consistently across all surfaces:

> "This is a standalone supporting track project, separate from core Support/QA/DE workflows."

- README.md L13: "This repo exists as a standalone supporting track, separate from the core Support/QA/DE wedge."
- portfolio-positioning.md L14: "This project operates in a separate supporting lane and does not compete with or claim to strengthen that primary wedge."
- landing/index.html L103: "This is a standalone supporting track project, separate from core Support/QA/DE workflows."
- demo/index.html L201: "Supporting PM-workflow document processor"

**No contradictions found.** All surfaces use consistent language describing the project as a supporting PM-workflow tool with no claims to the primary Support/QA/DE wedge.
