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
OWNER_COLUMN = "multiple_person_mm16b6ej"

HEADERS = {
    "Authorization": MONDAY_API_TOKEN,
    "Content-Type": "application/json"
}

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

contacts = apollo_response.json().get("contacts", [])

print(f"Found {len(contacts)} contacts")

for contact in contacts:

    name = contact.get("name", "")
    email = contact.get("email", "")
    title = contact.get("title", "")
    company = contact.get("organization_name", "")
    mobile = contact.get("sanitized_phone", "")

    if not email:
        continue

    search_query = f"""
    query {{
      boards(ids: [{BOARD_ID}]) {{
        items_page(
          limit: 10
          query_params: {{
            rules: [{{
              column_id: "{EMAIL_COLUMN}"
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
        headers=HEADERS,
        json={"query": search_query}
    )

    items = (
        search_response.json()
        .get("data", {})
        .get("boards", [{}])[0]
        .get("items_page", {})
        .get("items", [])
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

    if items:
