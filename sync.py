import os
import requests

APOLLO_API_KEY = os.environ["APOLLO_API_KEY"]
MONDAY_API_TOKEN = os.environ["MONDAY_API_TOKEN"]

BOARD_ID = 18395580962
EMAIL_COLUMN = "email_mm47srsd"

apollo_response = requests.post(
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

contacts = apollo_response.json().get("contacts", [])

if not contacts:
    print("No contacts found")
    raise SystemExit()

contact = contacts[0]

email = contact.get("email", "")
name = contact.get("name", "")

print("CONTACT:", name)
print("EMAIL:", email)

search_query = """
query ($board_id: ID!) {
  boards(ids: [$board_id]) {
    items_page(
      limit: 10
      query_params: {
        rules: [{
          column_id: "email_mm47srsd"
          compare_value: [\"EMAIL_PLACEHOLDER\"]
        }]
      }
    ) {
      items {
        id
        name
      }
    }
  }
}
"""

search_query = search_query.replace(
    "EMAIL_PLACEHOLDER",
    email
)

response = requests.post(
    "https://api.monday.com/v2",
    headers={
        "Authorization": MONDAY_API_TOKEN,
        "Content-Type": "application/json"
    },
    json={
        "query": search_query,
        "variables": {
            "board_id": BOARD_ID
        }
    }
)

print(response.text)
