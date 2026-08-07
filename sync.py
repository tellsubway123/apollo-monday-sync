import os
import requests
import json

APOLLO_API_KEY = os.environ["APOLLO_API_KEY"]

search_response = requests.post(
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

person = search_response.json()["people"][0]

print("PERSON ID:")
print(person["id"])
