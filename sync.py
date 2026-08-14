import os
import requests

APOLLO_API_KEY = os.environ["APOLLO_API_KEY"]

response = requests.get(
    "https://api.apollo.io/api/v1/emailer_campaigns/search",
    headers={
        "X-Api-Key": APOLLO_API_KEY
    }
)

campaigns = response.json().get("emailer_campaigns", [])

print("CAMPAIGNS FOUND:", len(campaigns))
print()

for campaign in campaigns:
    print(
        campaign.get("name"),
        "| USER_ID:",
        campaign.get("user_id")
    )
