# Operational Workflow for Tracking Pilots in DC4EU

This document defines the step-by-step process for maintaining accurate and up-to-date dashboards for Piloting Agents (PAs), SPOCs, and Coordinators.

---

## Objective

Ensure that three levels of visibility are always synchronised and consistent:

1. **Piloting Agent (PA)** – Progress and scenario documentation
2. **SPOC** – Consolidated view of all assigned PAs
3. **Project Coordinator** – Global view across all SPOCs and PAs

---

## Step 1 – Piloting Agent actions: document and update

| Task | Actor | Tools / Files |
|------|-------|----------------|
| Describe user journeys and context | PA | `PA-<name>/README.md` |
| Complete the checklist as implementation progresses | PA | `PA-<name>/PA-checklist.md` |
| Ensure folder is correctly named and committed | PA / SPOC | `PA-<institution>` folder |

✅ **Outcome**: Each PA has a self-contained folder with their scenario and progress.

---

## Step 2 – SPOC actions: supervise and validate

| Task | Actor | Tools / Files |
|------|-------|----------------|
| Review and validate user journeys in README | SPOC | `PA-<name>/README.md` |
| Complete the verification checklist | SPOC | `PA-<name>/SPOC-checklist.md` |
| Track issues, risks, and recommendations | SPOC | Directly in the checklist |
| Ensure alignment between PA documentation and real status | SPOC | Visual/manual or scripted validation |

✅ **Outcome**: SPOC provides assurance and oversight over PA documentation.

---

## Step 3 – Automation: extract and generate progress indicators

| Task | Actor | Tools / Scripts |
|------|-------|------------------|
| Run checklist parser to extract completion % and dates | SPOC or Coordinator | `repo_progress_parser.py` |
| Generate unified CSV of all PAs, with pilot, country, progress, status | Script | `piloting/OVERVIEW/indicators.csv` |
| Generate SPOC dashboards with live progress | Script | `generate_spoc_dashboards.py` → `SPOC-*/index.md` |
| Generate coordinator summary with SPOC-level status | Script | `generate_progress_summary.py` → `OVERVIEW/progress-summary.md` |

✅ **Outcome**: Real-time status tables are auto-generated for each SPOC and the whole project.

---

## Step 4 – Coordinator actions: global visibility

| Task | Actor | Tools / Files |
|------|-------|----------------|
| Review CSV file in spreadsheet or dashboard | Coordinator | `OVERVIEW/indicators.csv` |
| Review SPOC summary dashboards | Coordinator | `SPOC-*/index.md` |
| Review global summary of SPOC status | Coordinator | `OVERVIEW/progress-summary.md` |

✅ **Outcome**: The coordination team has a full picture of implementation across the network.

---

## Script Execution Order

```bash
# (Optional) If structure doesn't exist
python generate_repo_structure.py

# 1. Extract data from checklists
python repo_progress_parser.py

# 2. Generate SPOC dashboards
python generate_spoc_dashboards.py

# 3. Generate overall coordination summary
python generate_progress_summary.py
```
