# Sample Workflow: PRD to Task Assignments

This document walks through a concrete example of the Smart Document Processing Engine pipeline, showing input files, the command to run, and the resulting output with interpretation notes.

## 1. Input Files

### PRD Data (`data/prd_data.json`)

The Product Requirements Document defines the product being built. The sample PRD describes the **Hivel Insight Dashboard**, a tool for engineering KPI visibility.

**Structure:**
- `product_name`: The product identifier
- `objectives`: High-level goals for the product
- `user_personas`: Target user types and their needs
- `functional_requirements`: Features grouped by module
- `non_functional_requirements`: Performance, scalability, and security constraints
- `constraints`: Technical and business limitations

**Sample excerpt:**
```json
{
  "product_name": "Hivel Insight Dashboard",
  "objectives": [
    "Provide real-time visibility into software engineering KPIs...",
    "Identify productivity bottlenecks and suggest actionable insights...",
    "Automate daily standup reports and sprint reviews..."
  ],
  "functional_requirements": {
    "KPI Dashboard Module": [
      "Displays key metrics such as cycle time, deployment frequency...",
      "Supports historical trend visualization over 7, 30, and 90-day windows."
    ],
    "AI-based Insight Generator": [
      "Highlights anomalies (e.g., spike in change failure rate).",
      "Recommends action plans (e.g., optimize CI/CD pipeline)."
    ]
  }
}
```

### Engineer Profiles (`data/enineer_profile.json`)

Note: The filename contains a typo (`enineer` instead of `engineer`). This file defines the team members available for task assignment.

**Structure:**
- Array of engineer objects, each containing:
  - `name`: Engineer identifier
  - `role`: Job title
  - `skills`: Comma-separated skill list

**Full content:**
```json
[
  {"name": "John", "role": "Front-end Engineer", "skills": "React, Angular, Frontend"},
  {"name": "Alex", "role": "Back-end Engineer", "skills": "Python, Django, Backend"},
  {"name": "Rachel", "role": "Full-stack Engineer", "skills": "Node.js, MongoDB, Fullstack"},
  {"name": "Sarah", "role": "ML Engineer", "skills": "TensorFlow, PyTorch, Machine Learning"}
]
```

## 2. Running the Pipeline

### Command

```powershell
python main.py --mode basic --prd_file data/prd_data.json --engineers data/enineer_profile.json
```

### What Happens

1. **Document Ingestion**: The engine parses the PRD JSON and extracts structured sections.
2. **Section Extraction**: Identifies Objectives, Functional Requirements, and User Personas.
3. **Embedding Generation**: Uses MiniLM (`all-MiniLM-L6-v2`) to create semantic embeddings of requirements and engineer skills.
4. **Task Assignment**: Matches user stories to engineers based on skill similarity.

### Pipeline Log Evidence

The `outputs/pipeline.log` confirms the embedding model usage:

```
2024-10-19 08:52:38,109 - INFO - Use pytorch device_name: cpu
2024-10-19 08:52:38,109 - INFO - Load pretrained SentenceTransformer: all-MiniLM-L6-v2
2024-10-19 08:52:59,757 - INFO - Extracted sections: Objectives, Functional Requirements, User Personas
```

## 3. Output (`outputs/output.json`)

### Structure

The output file contains three main arrays:

| Field | Description |
|-------|-------------|
| `epics` | High-level feature groupings derived from functional requirements |
| `user_stories` | Individual requirements converted to user story format |
| `assignments` | Pairings of user stories to engineers |

### Full Output (Lines 1-36)

```json
{
  "epics": [
    "Epic: KPI Dashboard Module",
    "Epic: AI-based Insight Generator",
    "Epic: Sprint Progress Tracker",
    "Epic: Team Comparison View"
  ],
  "user_stories": [
    "As a user, I want Displays key metrics such as cycle time, deployment frequency, change failure rate, and MTTR. so that I can improve productivity.",
    "As a user, I want Supports historical trend visualization over 7, 30, and 90-day windows. so that I can improve productivity.",
    "As a user, I want Highlights anomalies (e.g., spike in change failure rate). so that I can improve productivity.",
    "As a user, I want Recommends action plans (e.g., optimize CI/CD pipeline). so that I can improve productivity.",
    "As a user, I want Automatically generates sprint progress updates. so that I can improve productivity.",
    "As a user, I want Tracks completed vs. pending stories for each sprint. so that I can improve productivity.",
    "As a user, I want Compares performance across multiple teams. so that I can improve productivity.",
    "As a user, I want Identifies outliers in productivity. so that I can improve productivity."
  ],
  "assignments": [
    ["As a user, I want Identifies outliers in productivity. so that I can improve productivity.", "Sarah"],
    ["As a user, I want Compares performance across multiple teams. so that I can improve productivity.", "Rachel"],
    ["As a user, I want Tracks completed vs. pending stories for each sprint. so that I can improve productivity.", "Alex"],
    ["As a user, I want Automatically generates sprint progress updates. so that I can improve productivity.", "John"]
  ]
}
```

### Interpretation Notes

**Epics**: The engine derives epics directly from the functional requirement keys in the PRD. Each module becomes an epic.

**User Stories**: Functional requirements are transformed into a standard user story format:
- Format: `"As a user, I want [requirement] so that I can [benefit]."`
- The benefit clause defaults to `"improve productivity"` for all stories in this sample.

**Assignments**: The engine pairs stories with engineers based on semantic similarity between the story text and engineer skills. For example:
- Sarah (ML Engineer) gets assigned anomaly detection tasks
- John (Front-end Engineer) gets assigned dashboard-related tasks
- Alex (Back-end Engineer) gets assigned data tracking tasks
- Rachel (Full-stack Engineer) gets assigned cross-team comparison tasks

## 4. Caveats

### Mixed Content in output.json

The `outputs/output.json` file contains **mixed content**. Lines 1-36 contain valid JSON. After line 36, the file contains schedule notes in a non-JSON format:

```
# [2022-12-27] (Embeddings) schedule note: Improve document extraction for Embeddings
# [2022-12-28] (Extraction) schedule note: Tune embedding scoring for Extraction
...
```

**Implication**: The file is not valid JSON end-to-end. JSON parsers will fail if they attempt to parse the entire file. Only lines 1-36 should be treated as JSON data.

### Schedule Notes

Both input files (`prd_data.json` and `enineer_profile.json`) and the output file contain appended schedule notes. These appear to be development tracking entries and are not part of the core data model.

### Filename Typo

The engineer profile file is named `enineer_profile.json` (missing the 'g' in engineer). Commands must use this exact spelling.

## 5. Verification

To verify the workflow ran successfully:

```powershell
# Check for output file
Select-String -Path "outputs/output.json" -Pattern "epics"

# Check for pipeline log
Select-String -Path "outputs/pipeline.log" -Pattern "MiniLM"
```

Expected results:
- `output.json` contains the `"epics"` array
- `pipeline.log` shows `all-MiniLM-L6-v2` model loading
