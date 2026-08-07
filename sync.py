import os
import requests

MONDAY_TOKEN = os.environ["MONDAY_API_TOKEN"]

query = """
mutation ($board_id: ID!, $group_id: String!, $item_name: String!) {
  create_item(
    board_id: $board_id,
    group_id: $group_id,
    item_name: $item_name
  ) {
    id
  }
}
"""

variables = {
    "board_id": 18395580962,
    "group_id": "group_mm582fdj",
    "item_name": "Workspace Test"
}

response = requests.post(
    "https://api.monday.com/v2",
    headers={
        "Authorization": MONDAY_TOKEN,
        "Content-Type": "application/json"
    },
    json={
        "query": query,
        "variables": variables
    }
)

print(response.status_code)
print(response.text)
