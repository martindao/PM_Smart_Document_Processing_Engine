# Architecture Overview

## Document Processing Pipeline

The Smart Document Processing Engine transforms PRD documents and engineer profiles into structured task assignments through a configurable NLP pipeline.

```mermaid
flowchart TB
    subgraph Input["Input Documents"]
        PRD["PRD JSON<br/>(objectives, requirements, personas)"]
        ENG["Engineer Profiles JSON<br/>(names, skills, capacity)"]
    end

    subgraph Ingestion["Data Ingestion"]
        INJ["PRDIngestionJSON<br/>(utils.py)"]
        LEN["load_engineers()<br/>(utils.py)"]
    end

    subgraph Mode["Pipeline Mode Selection"]
        M1["Basic Mode<br/>(BasicNLPModel)"]
        M2["Advanced Mode<br/>(AdvancedNLPModel)"]
        M3["Optimized Mode<br/>(ReinforcementLearningModel)"]
    end

    subgraph Extraction["Section Extraction"]
        EXT["extract_sections()<br/>(models.py)"]
    end

    subgraph Generation["Epic & Story Generation"]
        GEN["generate_epics_and_stories()<br/>(utils.py)"]
    end

    subgraph Assignment["Task Assignment"]
        ASG["assign_tasks()<br/>(models.py)"]
        OPT["optimize_workload_knapsack()<br/>(optimization.py)"]
    end

    subgraph Output["Output Artifacts"]
        JSON["JSON Output<br/>(epics, stories, assignments)"]
        CSV["CSV Output<br/>(assignments table)"]
        EDA["EDA Plots<br/>(prd_overview.png)"]
        LOG["Pipeline Logs"]
    end

    PRD --> INJ
    ENG --> LEN
    INJ --> EXT
    LEN --> ASG

    EXT --> GEN
    GEN --> ASG

    ASG --> JSON
    ASG --> CSV

    M1 -.->|rule-based| ASG
    M2 -.->|MiniLM embeddings| ASG
    M3 -.->|embeddings + optimization| OPT
    OPT --> ASG

    ASG --> EDA
    ASG --> LOG
```

## Pipeline Modes

| Mode | Model Class | Assignment Strategy |
|------|-------------|---------------------|
| `basic` | `BasicNLPModel` | Round-robin distribution across engineers |
| `advanced` | `AdvancedNLPModel` | MiniLM (all-MiniLM-L6-v2) semantic similarity matching |
| `optimized` | `ReinforcementLearningModel` | Embeddings + knapsack dynamic programming optimization |

## Component Reference

### Data Ingestion (`utils.py`)

- **`PRDIngestionJSON`**: Loads and parses PRD JSON files containing objectives, functional requirements, and user personas
- **`load_engineers()`**: Reads engineer profile JSON with skills and capacity data

### NLP Models (`models.py`)

- **`BasicNLPModel`**: Rule-based extraction and round-robin task assignment
- **`AdvancedNLPModel`**: Uses SentenceTransformer embeddings for semantic matching between stories and engineer skills
- **`ReinforcementLearningModel`**: Extends advanced model with optimization layer

### Optimization (`optimization.py`)

- **`optimize_workload_knapsack()`**: Dynamic programming approach to balance workload distribution while maximizing skill-task alignment scores

### Utilities (`utils.py`)

- **`generate_epics_and_stories()`**: Transforms functional requirements into epics and user stories
- **`save_output()`**: Exports results to JSON and CSV formats
- **`evaluate_assignments()`**: Computes precision, recall, F1, BLEU, and ROUGE metrics
- **`perform_eda()`**: Generates exploratory data analysis visualizations

### Entry Points

- **`main.py`**: CLI interface with `--mode`, `--prd_file`, and `--engineers` arguments
- **`app.py`**: Streamlit web interface with interactive mode selection and download buttons

## Data Flow

1. **Load**: PRD and engineer profiles are read from JSON files
2. **Extract**: NLP model extracts relevant sections (objectives, requirements, personas)
3. **Generate**: Functional requirements are converted to epics and user stories
4. **Assign**: Tasks are matched to engineers based on selected mode
5. **Optimize** (if `optimized` mode): Knapsack DP rebalances assignments
6. **Evaluate**: Assignment quality metrics are computed
7. **Export**: Results saved as JSON, CSV, and visualization plots
