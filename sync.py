import os
import requests

APOLLO_API_KEY = os.environ["APOLLO_API_KEY"]

CONTACT_ID = "6a2ad3d528506200010ef488"

response = requests.get(
    f"https://api.apollo.io/api/v1/contacts/{CONTACT_ID}",
    headers={
        "X-Api-Key": APOLLO_API_KEY
    }
)

print("STATUS:", response.status_code)
print(response.text)
