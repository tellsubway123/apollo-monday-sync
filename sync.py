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
        "q_keywords": "Julie Durose",
        "page": 1,
        "per_page": 10
    }
)

print(json.dumps(response.json(), indent=2)[:15000])
