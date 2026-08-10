import os
import json
import requests

APOLLO_API_KEY = os.environ["APOLLO_API_KEY"]
MONDAY_API_TOKEN = os.environ["MONDAY_API_TOKEN"]

BOARD_ID = 18395580962
GROUP_ID = "group_mm582fdj"
OWNER_ID = 103624857

EMAIL_COLUMN = "email_mm47srsd"
ACCOUNT_COLUMN = "text_mkzm1fns"
TITLE_COLUMN = "text_mkzmfmqb"
MOBILE_COLUMN = "phone_mkzmcmj7"
CORPORATE_COLUMN = "phone_mm47z80h"
OWNER_COLUMN = "multiple_person_mm16b6ej"

response = requests.post(
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

contacts = response.json().get("contacts", [])

print(f"Found {len(contacts)} contacts")

for contact in contacts:

    name = contact.get("name", "")
    email = contact.get("email", "")
    title = contact.get("title", "")
    company = contact.get("organization_name", "")
    mobile = contact.get("sanitized_phone", "")

    print("Processing:", name)

    monday_query = """
    query ($board_id: ID!) {
      boards(ids: [$board_id]) {
        id
      }
    }
    """

    monday_response = requests.post(
        "https://api.monday.com/v2",
        headers={
            "Authorization": MONDAY_API_TOKEN,
            "Content-Type": "application/json"
        },
        json={
            "query": monday_query,
            "variables": {
                "board_id": BOARD_ID
            }
        }
    )

    column_values = {
        ACCOUNT_COLUMN: company,
        TITLE_COLUMN: title,
        EMAIL_COLUMN: {
            "email": email,
            "text": email
        },
        MOBILE_COLUMN: {
            "phone": mobile,
            "countryShortName": "US"
        },
        OWNER_COLUMN: {
            "personsAndTeams": [
                {
                    "id": OWNER_ID,
                    "kind": "person"
                }
            ]
        }
    }

    create_mutation = """
    mutation ($board_id: ID!, $group_id: String!, $item_name: String!, $column_values: JSON!) {
      create_item(
        board_id: $board_id,
        group_id: $group_id,
        item_name: $item_name,
        column_values: $column_values
      ) {
        id
      }
    }
    """

    result = requests.post(
        "https://api.monday.com/v2",
        headers={
            "Authorization": MONDAY_API_TOKEN,
            "Content-Type": "application/json"
        },
        json={
            "query": create_mutation,
            "variables": {
                "board_id": BOARD_ID,
                "group_id": GROUP_ID,
                "item_name": name,
                "column_values": json.dumps(column_values)
            }
        }
    )

    print(result.text)
