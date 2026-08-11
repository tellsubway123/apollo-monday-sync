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
        "per_page": 100,
        "sort_by_field": "updated_at",
        "sort_ascending": False
    }
)

contacts = response.json().get("contacts", [])

for contact in contacts:

    print(
        contact.get("name"),
        "|",
        contact.get("updated_at")
    )
