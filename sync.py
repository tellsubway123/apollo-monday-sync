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
        "creator_ids": ["6a171a990217cf001039ff2a"],
        "page": 1,
        "per_page": 20
    }
)

print(json.dumps(response.json(), indent=2)["6a171a990217cf001039ff2a20
