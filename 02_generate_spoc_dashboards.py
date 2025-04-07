import os
import pandas as pd
from datetime import datetime

# Define root directory
ROOT_DIR = "./piloting"
INDICATOR_FILE = os.path.join(ROOT_DIR, "OVERVIEW", "indicators.csv")

# Read indicators CSV
if not os.path.exists(INDICATOR_FILE):
    raise FileNotFoundError("Run repo_progress_parser.py first to generate indicators.csv")

# Load data
df = pd.read_csv(INDICATOR_FILE)

# Helper to find SPOC folder names
spoc_folders = [d for d in os.listdir(ROOT_DIR) if d.startswith("SPOC-")]

# Try to map PAs to SPOC folders based on SPOC name in indicators.csv
for spoc_folder in spoc_folders:
    spoc_name = spoc_folder.replace("SPOC-", "").replace("_", " ").replace("and", "&")
    spoc_path = os.path.join(ROOT_DIR, spoc_folder)
    output_file = os.path.join(spoc_path, "index.md")

    # Filter rows where the SPOC name matches
    spoc_data = df[df['SPOC'].str.lower() == spoc_name.lower()]

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# SPOC Dashboard – {spoc_name}\n\n")
        f.write("| Piloting Agent | Country | Pilot | Checklist % | Last Update | Status |\n")
        f.write("|----------------|---------|--------|--------------|-------------|--------|\n")
        for _, row in spoc_data.iterrows():
            f.write(f"| {row['PA']} | {row['Country']} | {row['Pilot Option']} | {row['Checklist Completion %']}% | {row['Last Update']} | {row['Status']} |\n")

print("✅ SPOC dashboards generated in each SPOC folder.")

