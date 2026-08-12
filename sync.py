import os
import requests

APOLLO_API_KEY = os.environ["APOLLO_API_KEY"]

CAMPAIGN_ID = "67b5c2b49d091d0011b11e06"

for page in [1, 2, 3]:

    response = requests.post(
        "https://api.apollo.io/api/v1/contacts/search",
        headers={
            "X-Api-Key": APOLLO_API_KEY,
            "Content-Type": "application/json"
        },
        json={
            "emailer_campaign_ids": [CAMPAIGN_ID],
            "page": page,
            "per_page": 100
        }
    )

    contacts = response.json().get("contacts", [])

    print("PAGE", page, "COUNT", len(contacts))
