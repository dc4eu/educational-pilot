import os
import pandas as pd
from datetime import datetime

# Set the base path of the piloting directory
ROOT_DIR = "./piloting"

# Initialise list to hold extracted progress data
progress_data = []

# Define helper function to extract checklist completion % and last modified date
def extract_checklist_info(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        total = content.count("- [")
        checked = content.count("- [x]") + content.count("- [X]")
        percent_complete = round((checked / total) * 100, 1) if total > 0 else 0
        last_update = datetime.fromtimestamp(os.path.getmtime(filepath)).strftime('%Y-%m-%d')
        return percent_complete, last_update
    except Exception:
        return 0, "N/A"

# Traverse all PA folders
for pa_dir in os.listdir(ROOT_DIR):
    full_path = os.path.join(ROOT_DIR, pa_dir)
    if os.path.isdir(full_path) and pa_dir.startswith("PA-"):
        pa_name = pa_dir.replace("PA-", "")

        # Files to extract from
        spoc_file = os.path.join(full_path, "SPOC-checklist.md")
        pa_file = os.path.join(full_path, "PA-checklist.md")
        readme_file = os.path.join(full_path, "README.md")

        spoc_completion, spoc_date = extract_checklist_info(spoc_file)
        pa_completion, pa_date = extract_checklist_info(pa_file)

        pilot_option = "Unknown"
        country = "Unknown"

        if os.path.exists(readme_file):
            with open(readme_file, 'r', encoding='utf-8') as f:
                content = f.read().lower()
                if "pilot 1" in content:
                    pilot_option = "Pilot 1"
                elif "pilot 2" in content:
                    pilot_option = "Pilot 2"
                elif "pilot 3" in content:
                    pilot_option = "Pilot 3"

        progress_data.append({
            "PA": pa_name,
            "Pilot Option": pilot_option,
            "PA Checklist %": pa_completion,
            "PA Last Update": pa_date,
            "SPOC Checklist %": spoc_completion,
            "SPOC Last Update": spoc_date,
            "Country": country
        })

# Create DataFrame and save to CSV
df = pd.DataFrame(progress_data)
output_file = os.path.join(ROOT_DIR, "OVERVIEW", "indicators.csv")
df.to_csv(output_file, index=False)
print(f"✔️ Progress data saved to {output_file}")

