import os
import requests

APOLLO_API_KEY = os.environ["APOLLO_API_KEY"]

campaign_response = requests.get(
    "https://api.apollo.io/api/v1/emailer_campaigns/search",
    headers={
        "X-Api-Key": APOLLO_API_KEY
    }
)

campaigns = campaign_response.json().get("emailer_campaigns", [])

campaign_ids = [campaign["id"] for campaign in campaigns]

print("CAMPAIGNS:", len(campaign_ids))

contact_ids = set()
contact_names = set()

for campaign_id in campaign_ids:

    response = requests.post(
        "https://api.apollo.io/api/v1/contacts/search",
        headers={
            "X-Api-Key": APOLLO_API_KEY,
            "Content-Type": "application/json"
        },
        json={
            "emailer_campaign_ids": [campaign_id],
            "page": 1,
            "per_page": 100
        }
    )

    contacts = response.json().get("contacts", [])

    print(campaign_id, "->", len(contacts))

    for contact in contacts:
        contact_ids.add(contact.get("id"))
        contact_names.add(contact.get("name"))

print()
print("UNIQUE CONTACT IDS:", len(contact_ids))
print("UNIQUE CONTACTS:", len(contact_names))
