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
        "per_page": 100
    }
)

data = response.json()

print("KEYS:")
print(data.keys())

print()

print("TOTAL CONTACTS:")
print(len(data.get("contacts", [])))
