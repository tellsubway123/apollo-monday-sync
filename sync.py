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

new_count = 0

for contact in contacts:

    contact_id = contact.get("id")
    name = contact.get("name")

    if contact_id in processed_contacts:

        print("SKIP |", name)

    else:

        print("NEW  |", name)

        processed_contacts.append
