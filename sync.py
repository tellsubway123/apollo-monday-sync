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
        "q_keywords": "Julie Durose",
        "page": 1,
        "per_page": 1
    }
)

contact = response.json()["contacts"][0]

print("NAME:", contact.get("name"))

for status in contact.get("contact_campaign_statuses", []):
    print("ADDED BY:", status.get("added_by_user_id"))
    print("ADDED AT:", status.get("added_at"))
    print("CAMPAIGN:", status.get("emailer_campaign_id"))
