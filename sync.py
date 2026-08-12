import os
import json
import requests

APOLLO_API_KEY = os.environ["APOLLO_API_KEY"]

PROCESSED_FILE = "processed_contacts.json"
MAX_NEW_CONTACTS = 10

with open(PROCESSED_FILE, "r") as f:
    processed_contacts = json.load(f)

processed_set = set(processed_contacts)

campaign_response = requests.get(
    "https://api.apollo.io/api/v1/emailer_campaigns/search",
    headers={
        "X-Api-Key": APOLLO_API_KEY
    }
)

campaigns = campaign_response.json().get("emailer_campaigns", [])

print("CAMPAIGNS FOUND:", len(campaigns))

unique_contacts = {}
new_contacts = []

for campaign in campaigns:

    campaign_id = campaign["id"]
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

        if len(contacts) == 0:
            break

        for contact in contacts:

            contact_id = contact.get("id")

            if contact_id:
                unique_contacts[contact_id] = contact

        page += 1

print("UNIQUE CONTACTS FOUND:", len(unique_contacts))

for contact_id, contact in unique_contacts.items():

    if contact_id in processed_set:
        continue

    new_contacts.append(contact)

print("UNPROCESSED CONTACTS:", len(new_contacts))

processed_this_run = 0

for contact in new_contacts:

    if processed_this_run >= MAX_NEW_CONTACTS:
        break

    contact_id = contact.get("id")
    name = contact.get("name")
    email = contact.get("email")

    print("PROCESS:", name, "|", email)

    processed_contacts.append(contact_id)
    processed_set.add(contact_id)

    processed_this_run += 1

with open(PROCESSED_FILE, "w") as f:
    json.dump(processed_contacts, f, indent=2)

print()
print("PROCESSED THIS RUN:", processed_this_run)
print("TOTAL STORED IDS:", len(processed_contacts))
