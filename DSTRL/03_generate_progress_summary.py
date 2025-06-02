import os
import pandas as pd

# Define input and output paths
ROOT_DIR = "./piloting"
INDICATOR_FILE = os.path.join(ROOT_DIR, "OVERVIEW", "indicators.csv")
SUMMARY_FILE = os.path.join(ROOT_DIR, "OVERVIEW", "progress-summary.md")

# Read indicators
if not os.path.exists(INDICATOR_FILE):
    raise FileNotFoundError("indicators.csv not found. Run repo_progress_parser.py first.")

# Load data
df = pd.read_csv(INDICATOR_FILE)

# Group by SPOC and summarise
summary = df.groupby("SPOC").agg({
    "PA": "count",
    "Checklist Completion %": [
        (lambda x: (x >= 80).sum()),  # On Track
        (lambda x: ((x > 0) & (x < 80)).sum()),  # At Risk
        (lambda x: (x == 0).sum()),  # Blocked
        "mean"
    ]
}).reset_index()
summary.columns = ["SPOC", "# PAs", "On Track", "At Risk", "Blocked", "Avg Progress (%)"]
summary["Avg Progress (%)"] = summary["Avg Progress (%)"].round(1)

# Write summary to markdown
with open(SUMMARY_FILE, 'w', encoding='utf-8') as f:
    f.write("# DC4EU Piloting – Global Progress Overview\n\n")
    f.write("| SPOC | # PAs | On Track | At Risk | Blocked | Avg Progress (%) |\n")
    f.write("|------|--------|----------|---------|---------|------------------|\n")
    for _, row in summary.iterrows():
        f.write(f"| {row['SPOC']} | {row['# PAs']} | {row['On Track']} | {row['At Risk']} | {row['Blocked']} | {row['Avg Progress (%)']} |\n")

print("✅ progress-summary.md has been generated.")

