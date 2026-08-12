import os
import requests

APOLLO_API_KEY = os.environ["APOLLO_API_KEY"]

for endpoint in [
    "https://api.apollo.io/api/v1/sequences",
    "https://api.apollo.io/api/v1/emailer_campaigns/search",
    "https://api.apollo.io/api/v1/emailer_campaigns/searches"
]:
    try:
        response = requests.get(
            endpoint,
            headers={"X-Api-Key": APOLLO_API_KEY}
        )

        print()
        print("ENDPOINT:", endpoint)
        print("STATUS:", response.status_code)
        print(response.text[:500])
    except Exception as e:
        print(endpoint, str(e))
