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
        "q_keywords": "Julie Durose",
        "page": 1,
        "per_page": 1
    }
)

contact = response.json()["contacts"][0]

for key in sorted(contact.keys()):
    print(key)
