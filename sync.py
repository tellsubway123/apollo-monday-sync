import os
import json
import requests

APOLLO_API_KEY = os.environ["APOLLO_API_KEY"]
MONDAY_API_TOKEN = os.environ["MONDAY_API_TOKEN"]

BOARD_ID = 18395580962
GROUP_ID = "group_mm582fdj"
OWNER_ID = 103624857

response = requests.post(
    "https://api.apollo.io/api/v1/contacts/search",
    headers={
        "X-Api-Key": APOLLO_API_KEY,
        "Content-Type": "application/json"
    },
    json={
        "page": 1,
        "per_page": 1,
        "sort_by_field": "created_at",
        "sort_ascending": False
    }
)

contact = response.json()["contacts"][0]

email = contact.get("email", "")
title = contact.get("title", "")
company = contact.get("organization_name", "")
mobile = contact.get("sanitized_phone", "")
name = contact.get("name", "")

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

print("MATCHES:", len(items))

values = {
    "text_mkzmfmqb": title,
    "text_mkzm1fns": company,
    "email_mm47srsd": {
        "email": email,
        "text": email
    },
    "phone_mkzmcmj7": {
        "phone": mobile,
        "countryShortName": "US"
    },
    "multiple_person_mm16b6ej": {
        "personsAndTeams": [
            {
                "id": OWNER_ID,
                "kind": "person"
            }
        ]
    }
}

if items:

    item_id = items[0]["id"]

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
        headers={
            "Authorization": MONDAY_API_TOKEN,
            "Content-Type": "application/json"
        },
        json={
            "query": mutation,
            "variables": {
                "board_id": BOARD_ID,
                "item_id": item_id,
                "column_values": json.dumps(values)
            }
        }
    )

    print("UPDATED")
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

    create_response = requests.post(
        "https://api.monday.com/v2",
        headers={
            "Authorization": MONDAY_API_TOKEN,
            "Content-Type": "application/json"
        },
        json={
            "query": mutation,
            "variables": {
                "board_id": BOARD_ID,
                "group_id": GROUP_ID,
                "item_name": name,
                "column_values": json.dumps(values)
            }
        }
    )

    print("CREATED")
    print(create_response.text)
