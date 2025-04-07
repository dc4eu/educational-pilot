import os
import pandas as pd
from datetime import datetime
import re
import yaml

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

# Define helper to infer pilot option and country from README frontmatter
def extract_metadata(filepath):
    pilot_option = "Unknown"
    country = "Unknown"
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
            if match:
                metadata = yaml.safe_load(match.group(1))
                pilot_option = metadata.get("pilot", pilot_option)
                country = metadata.get("country", country)
            else:
                # fallback keyword matching
                content = content.lower()
                if "pilot 1" in content:
                    pilot_option = "Pilot 1"
                elif "pilot 2" in content:
                    pilot_option = "Pilot 2"
                elif "pilot 3" in content:
                    pilot_option = "Pilot 3"
    except Exception:
        pass
    return pilot_option, country

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
        pilot_option, country = extract_metadata(readme_file)

        # Infer status
        if pa_completion >= 80:
            status = "On Track"
        elif pa_completion > 0:
            status = "At Risk"
        else:
            status = "Blocked"

        progress_data.append({
            "SPOC": "TBD",  # can be filled in or parsed separately if needed
            "PA": pa_name,
            "Country": country,
            "Pilot Option": pilot_option,
            "Checklist Completion %": pa_completion,
            "Last Update": pa_date,
            "Status": status
        })

# Create DataFrame and save to CSV
df = pd.DataFrame(progress_data)
output_file = os.path.join(ROOT_DIR, "OVERVIEW", "indicators.csv")
df.to_csv(output_file, index=False)
print(f"✔️ Enriched progress data saved to {output_file}")

