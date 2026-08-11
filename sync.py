import os
import requests

APOLLO_API_KEY = os.environ["APOLLO_API_KEY"]

response = requests.post(
    "https://api.apollo.io/api/v1/contacts/search",
    headers={
        "X-Api-Key": APOLLO_API_KEY,
        "Content-Type": "application/json"
    },
    json={
        "page": 1,
        "per_page": 20
    }
)

contacts = response.json().get("contacts", [])

for contact in contacts:
    print(
        contact.get("name"),
        "| owner:",
        contact.get("owner_id"),
        "| creator:",
        contact.get("creator_id")
    )
