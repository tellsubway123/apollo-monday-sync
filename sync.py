import os
import requests

MONDAY_API_TOKEN = os.environ["MONDAY_API_TOKEN"]

query = """
query {
  boards(ids: 18395580962) {
    columns {
      id
      title
      type
    }
  }
}
"""

response = requests.post(
    "https://api.monday.com/v2",
    headers={
        "Authorization": MONDAY_API_TOKEN,
        "Content-Type": "application/json"
    },
    json={
        "query": query
    }
)

print(response.text)
