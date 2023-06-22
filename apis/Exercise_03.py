'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''
import requests
from pprint import pprint

url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "first_name": "Mr.",
    "last_name": "Crabs",
    "email": "bikini@bottom.to"
}

response = requests.post(url, json=body)

print(f"Response Code; {response.status_code}")

response = requests.get(url)

pprint(response.json())