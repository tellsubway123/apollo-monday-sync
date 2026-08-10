import os
import json
import requests
from datetime import datetime

APOLLO_API_KEY = os.environ["APOLLO_API_KEY"]
MONDAY_API_TOKEN = os.environ["MONDAY_API_TOKEN"]

BOARD_ID = 18395580962
GROUP_ID = "group_mm582fdj"
OWNER_ID = 103624857

ACCOUNT_COLUMN = "text_mkzm1fns"
TITLE_COLUMN = "text_mkzmfmqb"
EMAIL_COLUMN = "email_mm47srsd"
MOBILE_COLUMN = "phone_mkzmcmj7"
OWNER_COLUMN = "multiple_person_mm16b6ej"

LAST_PROCESSED_FILE = "last_processed.txt"

MONDAY_HEADERS = {
    "Authorization": MONDAY_API_TOKEN,
    "Content-Type": "application/json"
}

with open(LAST_PROCESSED_FILE, "r") as f:
    last_processed = f.read().strip()

last_processed_dt = datetime.fromisoformat(
    last_processed.replace("Z", "+00:00")
)

print("LAST PROCESSED:", last_processed)

apollo_response = requests.post(
    "https://api.apollo.io/api/v1/contacts/search",
    headers={
        "X-Api-Key": APOLLO_API_KEY,
        "Content-Type": "application/json"
    },
    json={
        "page": 1,
        "per_page": 10,
        "sort_by_field": "created_at",
        "sort_ascending": False
    }
)

apollo_response.raise_for_status()

all_contacts = apollo_response.json().get("contacts", [])

contacts = []

for contact in all_contacts:

    created_at = contact.get("created_at")

    if not created_at:
        continue

    created_dt = datetime.fromisoformat(
        created_at.replace("Z", "+00:00")
    )

    if created_dt > last_processed_dt:
        contacts.append(contact)

print(f"NEW CONTACTS FOUND: {len(contacts)}")

newest_timestamp = last_processed

for contact in contacts:

    created_at = contact.get("created_at")

    if created_at and created_at > newest_timestamp:
        newest_timestamp = created_at

    email = contact.get("email", "")
    name = contact.get("name", "")
    title = contact.get("title", "")
    company = contact.get("organization_name", "")
    mobile = contact.get("sanitized_phone", "")

    if not email:
        continue

    print(f"PROCESSING: {name}")

    search_query = f"""
    query {{
      boards(ids: [{BOARD_ID}]) {{
        items_page(
          limit: 10
          query_params: {{
            rules: [{{
              column_id:
