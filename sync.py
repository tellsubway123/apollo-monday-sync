import os
import json
import requests

APOLLO_API_KEY = os.environ["APOLLO_API_KEY"]

PROCESSED_FILE = "processed_contacts.json"

with open(PROCESSED_FILE, "r") as f:
    processed_contacts = json.load(f)

response = requests.post(
    "https://api.apollo.io/api/v1/contacts/search",
    headers={
        "X-Api-Key": APOLLO_API_KEY,
        "Content-Type": "application/json"
    },
    json={
        "owner_ids": ["6a171a990217cf001039ff2a"],
        "page": 1,
        "per_page": 20
    }
)

contacts = response.json().get("contacts", [])

print("PROCESSED IDS:", len(processed_contacts))
print("APOLLO CONTACTS:", len(contacts))

for contact in contacts:
    print(contact.get("id"), "|", contact.get("name"))
