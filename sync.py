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
        "emailer_campaign_ids": ["6a60cc79d0d4430020e6e356"],
        "page": 1,
        "per_page": 20
    }
)

print(json.dumps(response.json(), indent=2)[:5000])
