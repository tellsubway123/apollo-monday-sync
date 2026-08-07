import os
import requests
import json

APOLLO_API_KEY = os.environ["APOLLO_API_KEY"]

response = requests.get(
    "https://api.apollo.io/api/v1/people/59fe56a7a6da9861955e1ec1",
    headers={
        "X-Api-Key": APOLLO_API_KEY
    }
)

person = response.json()["person"]

print("EMAILS:")
print(person.get("emails"))

print("\nPHONE:")
print(person.get("phone"))

print("\nMOBILE_PHONE:")
print(person.get("mobile_phone"))

print("\nDIRECT_DIAL:")
print(person.get("direct_dial"))

print("\nORGANIZATION:")
print(person.get("organization", {}))
