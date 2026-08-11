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
        "page": 1,
        "per_page": 100
    }
)

data = response.json()

print("PAGINATION:")
print(json.dumps(data.get("pagination", {}), indent=2))

print()
print("NUM_FETCH_RESULT:")
print(data.get("num_fetch_result"))
