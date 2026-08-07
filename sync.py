import os
import requests

APOLLO_API_KEY = os.environ["APOLLO_API_KEY"]

response = requests.get(
    "https://api.apollo.io/api/v1/people/6a75e1f39598d700146166f3",
    headers={
        "X-Api-Key": APOLLO_API_KEY
    }
)

person = response.json()["person"]

print("NAME:", person.get("name"))
print("EMAIL:", person.get("email"))
print("TITLE:", person.get("title"))
print("COMPANY:", person.get("organization", {}).get("name"))
