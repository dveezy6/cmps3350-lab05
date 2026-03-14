import json
import sys

FILENAME = "lab_student_names.json"
REQUIRED_FIELDS = {"name", "github"}

try:
    with open(FILENAME, "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"ERROR: Could not find {FILENAME}")
    sys.exit(1)
except json.JSONDecodeError as e:
    print(f"ERROR: Invalid JSON - {e}")
    sys.exit(1)

if "students" not in data:
    print("ERROR: Missing top-level 'students' list")
    sys.exit(1)

if not isinstance(data["students"], list):
    print("ERROR: 'students' must be a list")
    sys.exit(1)

for i, entry in enumerate(data["students"], start=1):
    if not isinstance(entry, dict):
        print(f"ERROR in Entry {i}: Entry must be an object")
        sys.exit(1)

    entry_fields = set(entry.keys())

    missing = REQUIRED_FIELDS - entry_fields
    if missing:
        print(f"ERROR in Entry {i}: Missing field(s): {', '.join(sorted(missing))}")
        sys.exit(1)

    unexpected = entry_fields - REQUIRED_FIELDS
    if unexpected:
        print(f"ERROR in Entry {i}: Unexpected field(s): {', '.join(sorted(unexpected))}")
        sys.exit(1)

    for field in REQUIRED_FIELDS:
        value = entry[field]
        if not isinstance(value, str) or value.strip() == "":
            print(f"ERROR in Entry {i}: Field '{field}' must be a non-empty string")
            sys.exit(1)

print("Validation successful.")
