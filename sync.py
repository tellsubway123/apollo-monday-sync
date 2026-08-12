import os
import requests

APOLLO_API_KEY = os.environ["APOLLO_API_KEY"]

response = requests.get(
    "https://api.apollo.io/api/v1/emailer_campaigns",
    headers={
        "X-Api-Key": APOLLO_API_KEY
    }
)

print(response.status_code)
print(response.text[:5000])
