import os
import json
import requests

MONDAY_TOKEN = os.environ["MONDAY_API_TOKEN"]

query = """
mutation ($board_id: ID!, $item_name: String!) {
  create_item(
    board_id: $board_id,
    item_name: $item_name
  ) {
    id
  }
}
"""

variables = {
    "board_id": 18395580962,
    "item_name": "Apollo Sync Test"
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
