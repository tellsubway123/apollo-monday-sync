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
        "per_page": 5
    }
)

data = response.json()

for contact in data.get("contacts", []):
    print("NAME:", contact.get("name"))
    print("ID:", contact.get("id"))
    print("CREATED:", contact.get("created_at"))
    print("---")
