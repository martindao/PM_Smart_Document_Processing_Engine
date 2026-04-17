# Demo Artifact Pack

This directory contains demonstration artifacts for portfolio proof, showcasing the Smart Document Processing Engine's capabilities.

## Purpose

These artifacts demonstrate the engine's ability to:
- Parse and extract structured data from PRD documents
- Generate epics and user stories from product requirements
- Assign user stories to team members using NLP-based scoring

## Artifacts

### 1. Sample Input: `prd_data.json`

**Source:** `../../data/prd_data.json`

A sample Product Requirements Document (PRD) for "Hivel Insight Dashboard" containing:
- Product objectives
- User personas (CTO, Engineering Manager, Developer)
- Functional requirements organized by module (KPI Dashboard, AI Insight Generator, Sprint Progress Tracker, Team Comparison View)
- Non-functional requirements (performance, scalability, security)
- Constraints

### 2. Processing Output: `output.json`

**Source:** `../output.json`

The engine's structured output containing:
- **Epics** (lines 1-7): Four high-level feature groupings extracted from the PRD
- **User Stories** (lines 8-17): Eight user stories derived from functional requirements
- **Assignments** (lines 18-35): User stories matched to team members

**Note:** The output.json file contains mixed content:
- Lines 1-36: Valid JSON with epics, user stories, and assignments
- Lines 44+: Schedule notes from historical pipeline runs (prefixed with `#`)

When using this artifact, extract only the JSON portion (lines 1-36) for valid JSON parsing.

## Generation Date

Artifacts generated: 2026-04-17

## Provenance Summary

| Artifact | Original Path | Description |
|----------|---------------|-------------|
| prd_data.json | `data/prd_data.json` | Sample PRD input |
| output.json | `outputs/output.json` | Processing output with epics, stories, assignments |

## Usage

To reproduce these results:

```powershell
python main.py --input data/prd_data.json --output outputs/output.json
```

## Notes

- All data has been anonymized for portfolio demonstration
- No proprietary or sensitive information is included
- Schedule notes in output.json reflect historical pipeline operations and can be ignored for demo purposes

## Anonymization Guidelines

This section provides guidance for maintaining anonymization standards when updating or adding artifacts to this demo pack.

### Synthetic Names

The following names used in assignments are **synthetic placeholders**, not real individuals:
- Sarah
- Rachel
- Alex
- John

When adding new artifacts, use these or similar common placeholder names. Do not use real team member names, client names, or any personally identifiable information.

### Pre-Publish Checklist

Before adding new artifacts or updating existing ones, verify:

- [ ] **Person Names**: All names replaced with synthetic placeholders (e.g., Alex, Sarah, John, Rachel, Mike, Emma)
- [ ] **Company Information**: No client names, company identifiers, or brand-specific references
- [ ] **Contact Details**: No email addresses, phone numbers, or physical addresses
- [ ] **Project Identifiers**: No internal project codes, ticket numbers, or sprint IDs that could trace to real work
- [ ] **Schedule Notes**: Historical pipeline notes should not contain sensitive operational details, team member names, or proprietary process information
- [ ] **JSON Content**: Verify structured data does not embed PII in field values or descriptions
- [ ] **Dates**: Consider generalizing specific dates if they could identify real project timelines

### Mixed Content Caveat

The `output.json` file contains **mixed content** that requires careful handling:

| Lines | Content Type | Notes |
|-------|--------------|-------|
| 1-36 | Valid JSON | Structured epics, user stories, and assignments |
| 37-73 | Schedule notes | Historical pipeline logs prefixed with `#` |

**Important**: Only lines 1-36 constitute valid JSON. Lines 37+ are operational notes from historical pipeline runs and should be treated as non-structured metadata.

### Anonymization Review Process

When in doubt about whether content is safe to include:

1. Ask: "Could this information identify a specific person, company, or project?"
2. If yes, replace with a generic placeholder or remove entirely
3. Document the replacement in this README if it affects interpretation of the artifact
