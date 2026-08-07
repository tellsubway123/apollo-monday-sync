import os
import requests

APOLLO_API_KEY = os.environ["APOLLO_API_KEY"]

response = requests.get(
    "https://api.apollo.io/api/v1/people/59fe56a7a6da9861955e1ec1",
    headers={
        "X-Api-Key": APOLLO_API_KEY
    }
)

person = response.json()["person"]

print("NAME:", person.get("name"))
print("EMAIL:", person.get("email"))
print("TITLE:", person.get("title"))
print("COMPANY:", person.get("organization", {}).get("name"))
