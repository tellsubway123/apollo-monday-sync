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
        "per_page": 20
    }
)

contacts = response.json().get("contacts", [])

for contact in contacts:

    statuses = contact.get("contact_campaign_statuses", [])

    if statuses:

        print(contact.get("name"))
        print("ADDED BY:", statuses[0].get("added_by_user_id"))
        print("ADDED AT:", statuses[0].get("added_at"))
        print("---")
