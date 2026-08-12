import json

PROCESSED_FILE = "processed_contacts.json"

with open(PROCESSED_FILE, "w") as f:
    json.dump(
        [
            "apollo-test-1",
            "apollo-test-2",
            "apollo-test-3"
        ],
        f,
        indent=2
    )

print("WROTE TEST IDS")
