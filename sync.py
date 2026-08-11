import os
import json

PROCESSED_FILE = "processed_contacts.json"

with open(PROCESSED_FILE, "r") as f:
    processed_contacts = json.load(f)

print("PROCESSED CONTACTS:")
print(processed_contacts)
print("COUNT:", len(processed_contacts))
