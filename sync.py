import os
import json
import requests

APOLLO_API_KEY = os.environ["APOLLO_API_KEY"]
MONDAY_API_TOKEN = os.environ["MONDAY_API_TOKEN"]

PROCESSED_FILE = "processed_contacts.json"
MAX_NEW_CONTACTS = 10

BOARD_ID = 18395580962
GROUP_ID = "group_mm582fdj"
OWNER_ID = 103624857

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
    name = contact.get("name", "")
    email = contact.get("email", "")
    title = contact.get("title", "")
    company = contact.get("organization_name", "")
    phone = contact.get("sanitized_phone", "")

    print("PROCESS:", name, "|", email)

    if not email:

        print("SKIP NO EMAIL:", name)

        processed_contacts.append(contact_id)
        processed_set.add(contact_id)

        processed_this_run += 1
        continue

    search_query = f"""
    query {{
      boards(ids: [{BOARD_ID}]) {{
        items_page(
          limit: 10
          query_params: {{
            rules: [{{
              column_id: "email_mm47srsd"
              compare_value: ["{email}"]
            }}]
          }}
        ) {{
          items {{
            id
          }}
        }}
      }}
    }}
    """

    search_response = requests.post(
        "https://api.monday.com/v2",
        headers={
            "Authorization": MONDAY_API_TOKEN,
            "Content-Type": "application/json"
        },
        json={
            "query": search_query
        }
    )

    items = (
        search_response.json()["data"]["boards"][0]
        ["items_page"]["items"]
    )

    values = {
        "text_mkzmfmqb": title,
