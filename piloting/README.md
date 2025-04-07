# DC4EU Piloting Repository Overview

This repository contains the organisational and operational structure for monitoring, documenting, and coordinating piloting activities under the DC4EU project.

## Directory Structure

```
/piloting/
├── PA-<InstitutionName>/            # One folder per Piloting Agent (PA)
│   ├── README.md                     # Scenario description (based on scenario template)
│   ├── PA-checklist.md              # Filled by the PA to self-track progress
│   └── SPOC-checklist.md            # Filled by the SPOC to track and validate the PA
│
├── SPOC-<SPOCName>/                 # One folder per SPOC
│   └── index.md                      # Dashboard summarising the status of all PAs assigned
│
└── OVERVIEW/                        # Coordination-level summaries and analytics
    ├── progress-summary.md           # High-level summary across SPOCs
    └── indicators.csv                # Machine-readable KPI and progress table
```

---

## File Descriptions

### In each `PA-<InstitutionName>` folder:
- `README.md`: Describes the scenarios implemented by the PA.
- `PA-checklist.md`: Filled by the PA to track implementation progress.
- `SPOC-checklist.md`: Filled by the SPOC to assess and validate the PA.

### In each `SPOC-<SPOCName>` folder:
- `index.md`: Contains a summary table of the status of all PAs supervised by this SPOC.

### In the `OVERVIEW/` folder:
- `progress-summary.md`: Markdown file with a table showing progress by SPOC.
- `indicators.csv`: Structured table including SPOC, PA, country, pilot option, completion %, last update, and status.

---

## Automation
You can run the `generate_repo_structure.py` script to:
- Generate all PA folders and template files
- Set up SPOC folders
- Create the `OVERVIEW/` directory with placeholder files

Use the `repo_progress_parser.py` script to:
- Read and parse all checklist files
- Calculate completion % and last updated date
- Update the `indicators.csv` file for coordination

---

## Usage Instructions
1. Each PA fills in their `README.md` and `PA-checklist.md`
2. SPOCs review and complete `SPOC-checklist.md`
3. SPOCs update `index.md` with a snapshot dashboard
4. Coordinators run `repo_progress_parser.py` to generate KPIs

---

## Goal
This structure ensures:
- Transparency in progress across all pilots
- Clear responsibilities for PAs and SPOCs
- Readiness for automated tracking and analytics

> Maintained by DC4EU SPOC and Coordination Teams