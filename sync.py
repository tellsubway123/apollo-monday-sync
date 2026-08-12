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
        "q_keywords": "Dave Stewart",
        "page": 1,
        "per_page": 1
    }
)

contact = response.json()["contacts"][0]

print(json.dumps(
    contact.get("contact_campaign_statuses", []),
    indent=2
))
