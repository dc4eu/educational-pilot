
import json
from jsonschema import validate, ValidationError

# Load credential and schema
with open("MasterDegree-EBSI-VC-full-aligned-unsigned.json", "r") as f:
    credential = json.load(f)

with open("HigherEducationDiploma-EDC-W3C-Schema-updated.json", "r") as f:
    schema = json.load(f)

# Validate and report
try:
    validate(instance=credential, schema=schema)
    print("✅ Credential is valid and conforms to the updated EDC-W3C schema.")
except ValidationError as e:
    print("❌ Validation failed:")
    print(e.message)
    print("Path to error:", list(e.path))
