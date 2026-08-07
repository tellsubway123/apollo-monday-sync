import os
import requests

APOLLO_API_KEY = os.environ["APOLLO_API_KEY"]

response = requests.get(
    "https://api.apollo.io/api/v1/contacts/6a75e1f39598d700146166f3",
    headers={
        "X-Api-Key": APOLLO_API_KEY
    }
)

print("Status:", response.status_code)
print(response.text[:4000])
