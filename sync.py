import os
import json
import requests

APOLLO_API_KEY = os.environ["APOLLO_API_KEY"]

response = requests.post(
    "https://api.apollo.io/api/v1/contacts/search",
    headers={
        "X-Api-Key": APOLLO_API_KEY,
        "Content-Type": "application/json"
    },
    json={
        "emailer_campaign_ids": [
            "6a60cc79d0d4430020e6e356",
            "6a60cd15302179001cdd84e4"
        ],
        "page": 1,
        "per_page": 100
    }
)

data = response.json()

print("CONTACT COUNT:", len(data.get("contacts", [])))

for contact in data.get("contacts", []):
    print(contact.get("name"))
