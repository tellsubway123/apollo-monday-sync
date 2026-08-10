import os
import json
import requests

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

MONDAY_HEADERS = {
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

apollo_response.raise_for_status()

contacts = apollo_response.json().get("contacts", [])

print(f"Found {len(contacts)} contacts")

for contact in contacts:

    email = contact.get("email", "")
    name = contact.get("name", "")
    title = contact.get("title", "")
    company = contact.get("organization_name", "")
    mobile = contact.get("sanitized_phone", "")

    if not email:
        print(f"Skipping {name} (no email)")
        continue

    print(f"Processing {name}")

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
        headers=MONDAY_HEADERS,
        json={"query": search_query}
    )

    search_data = search_response.json()

    matches = (
        search_data
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

    column_values_json = json.dumps(column_values)

    if matches:

        item_id = matches[0]["id"]

        mutation = """
        mutation ($board_id: ID!, $item_id: ID!, $column_values: JSON!) {
          change_multiple_column_values(
            board_id: $board_id,
            item_id: $item_id,
            column_values: $column_values
          ) {
            id
          }
        }
        """

        update_response = requests.post(
            "https://api.monday.com/v2",
            headers=MONDAY_HEADERS,
            json={
                "query": mutation,
                "variables": {
                    "board_id": BOARD_ID,
                    "item_id": item_id,
                    "column_values": column_values_json
                }
            }
        )

        print(f"UPDATED: {name}")
        print(update_response.text)

    else:

        mutation = """
        mutation (
          $board_id: ID!,
          $group_id: String!,
          $item_name: String!,
          $column_values: JSON!
        ) {
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

        create_response 
