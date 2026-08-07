import os
import requests

APOLLO_API_KEY = os.environ["APOLLO_API_KEY"]

response = requests.post(
    "https://api.apollo.io/api/v1/mixed_people/api_search",
    headers={
        "X-Api-Key": APOLLO_API_KEY,
        "Content-Type": "application/json"
    },
    json={
        "page": 1,
        "per_page": 5
    }
)

print("Status:", response.status_code)

data = response.json()

for person in data.get("people", []):
    first = person.get("first_name", "")
    last = person.get("last_name", "")
    print(f"{first} {last}")
