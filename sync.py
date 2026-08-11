import os
import requests
import json

APOLLO_API_KEY = os.environ["APOLLO_API_KEY"]

response = requests.post(
    "https://api.apollo.io/api/v1/contacts/search",
    headers={
        "X-Api-Key": APOLLO_API_KEY,
        "Content-Type": "application/json"
    },
    json={
        "page": 1,
        "per_page": 100
    }
)

contacts = response.json().get("contacts", [])

for contact in contacts:
    name = str(contact.get("name", "")).lower()

    if "julie" in name:
        print(json.dumps(contact, indent=2))
