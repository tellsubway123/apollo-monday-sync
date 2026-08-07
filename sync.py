import os
import requests

api_key = os.environ["APOLLO_API_KEY"]

response = requests.post(
    "https://api.apollo.io/api/v1/mixed_people/search",
    headers={
        "X-Api-Key": api_key,
        "Content-Type": "application/json"
    },
    json={
        "page": 1,
        "per_page": 1
    }
)

print("Status Code:", response.status_code)
print(response.text[:500])
