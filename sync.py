import json

PROCESSED_FILE = "processed_contacts.json"

with open(PROCESSED_FILE, "w") as f:
    json.dump(
        [
            "test-id-1",
            "test-id-2"
        ],
        f,
        indent=2
    )

print("FILE UPDATED")
