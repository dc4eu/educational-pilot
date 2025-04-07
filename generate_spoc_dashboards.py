import os
import pandas as pd
from datetime import datetime

# Define root directory
ROOT_DIR = "./piloting"

# Read indicators CSV
indicators_path = os.path.join(ROOT_DIR, "OVERVIEW", "indicators.csv")
if not os.path.exists(indicators_path):
    raise FileNotFoundError("Run repo_progress_parser.py first to generate indicators.csv")

# Load data
df = pd.read_csv(indicators_path)

# Extract SPOC from folder structure or metadata later
# For now, this is inferred from folder structure or prefilled data
# Grouping logic can be improved if we standardize SPOC per PA elsewhere

# Helper to find SPOC folder names
spoc_folders = [d for d in os.listdir(ROOT_DIR) if d.startswith("SPOC-")]

# Try to map PAs to SPOC folders based on SPOC name in indicators.csv
for spoc_folder in spoc_folders:
    spoc_name = spoc_folder.replace("SPOC-", "").replace("_", " ").replace("and", "&")
    spoc_path = os.path.join(ROOT_DIR, spoc_folder)
    output_file = os.path.join(spoc_path, "index.md")

    # Filter PAs by SPOC name (case-insensitive partial match)
    spoc_data = df[df["PA"].str.contains("", na=False)]  # fallback
    for potential in df["PA"].unique():
        if spoc_name.lower() in potential.lower():
            spoc_data = df[df["PA"] == potential]
            break

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# SPOC Dashboard – {spoc_name}\n\n")
        f.write("| Piloting Agent | Country | Pilot | PA Checklist % | PA Last Update | SPOC Checklist % | SPOC Last Update |\n")
        f.write("|----------------|---------|--------|----------------|----------------|------------------|------------------|\n")
        for _, row in spoc_data.iterrows():
            f.write(f"| {row['PA']} | {row['Country']} | {row['Pilot Option']} | {row['PA Checklist %']}% | {row['PA Last Update']} | {row['SPOC Checklist %']}% | {row['SPOC Last Update']} |\n")

print("✅ SPOC dashboards generated in each SPOC folder.")

