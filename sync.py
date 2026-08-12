import os
import requests

APOLLO_API_KEY = os.environ["APOLLO_API_KEY"]

# Get all campaigns
campaign_response = requests.get(
    "https://api.apollo.io/api/v1/emailer_campaigns/search",
    headers={
        "X-Api-Key": APOLLO_API_KEY
    }
)

campaigns = campaign_response.json().get("emailer_campaigns", [])

print("TOTAL CAMPAIGNS:", len(campaigns))

unique_contact_ids = set()

for campaign in campaigns:

    campaign_id = campaign["id"]
    campaign_name = campaign.get("name", campaign_id)

    campaign_count = 0
    page = 1

    while True:

        response = requests.post(
            "https://api.apollo.io/api/v1/contacts/search",
            headers={
                "X-Api-Key": APOLLO_API_KEY,
                "Content-Type": "application/json"
            },
            json={
                "emailer_campaign_ids": [campaign_id],
                "page": page,
                "per_page": 100
            }
        )

        contacts = response.json().get("contacts", [])

        count = len(contacts)

        if count == 0:
            break

        campaign_count += count

        for contact in contacts:
            unique_contact_ids.add(contact.get("id"))

        page += 1

    print(f"{campaign_name} -> {campaign_count}")

print()
print("TOTAL UNIQUE CONTACT IDS:", len(unique_contact_ids))
