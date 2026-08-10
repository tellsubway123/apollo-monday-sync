import os
import json
import requests

APOLLO_API_KEY = os.environ["APOLLO_API_KEY"]
MONDAY_API_TOKEN = os.environ["MONDAY_API_TOKEN"]

BOARD_ID = 18395580962

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
name = contact.get("name", "")
title = contact.get("title", "")
company = contact.get("organization_name", "")

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
        name
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
    json={"query": search_query}
)

search_data = search_response.json()

items = (
    search_data["data"]["boards"][0]
    ["items_page"]["items"]
)

print("Matches Found:", len(items))

if items:
    print("Existing Monday Item:", items[0]["id"])
else:
    print("No matching item found")
