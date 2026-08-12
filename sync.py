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
        "added_by["APOLLO_API_KEY"_user_ids": 01039ff2a"],
        "page": 1,
        "per_page": 20
    }
)

print(json.dumps(response.json(), indent=2)[:5000])
