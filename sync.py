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
        "per_page": 1,
        "sort_by_field": "created_at",
        "sort_ascending": False
    }
)

contact = response.json()["contacts"][0]

print("NAME:", contact.get("name"))
print("EMAIL:", contact.get("email"))
print("TITLE:", contact.get("title"))
print("COMPANY:", contact.get("organization_name"))
print("MOBILE:", contact.get("sanitized_phone"))
