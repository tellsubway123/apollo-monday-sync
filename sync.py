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
        "per_page": 10,
        "sort_by_field": "created_at",
        "sort_ascending": False
    }
)

print("Status:", response.status_code)
print(response.text[:4000])
