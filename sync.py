import os
import requests
import json

APOLLO_API_KEY = os.environ["APOLLO_API_KEY"]

response = requests.post(
    "https://api.apollo.io/api/v1/mixed_people/api_search",
    headers={
        "X-Api-Key": APOLLO_API_KEY,
        "Content-Type": "application/json"
    },
    json={
        "page": 1,
        "per_page": 1
    }
)

print("Status:", response.status_code)

data = response.json()

people = data.get("people", [])

if people:
    print(json.dumps(people[0], indent=2))
