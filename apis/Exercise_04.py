'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''

import requests
from pprint import pprint

url = "http://demo.codingnomads.co:8080/tasks_api/users/721"

body = {
    "first_name": "Mr.",
    "last_name": "Crabs",
    "email": "bikini@bottom.io"
}

response = requests.put(url, json=body)

print(response.status_code)

response = requests.get(base_url +"/721")

pprint(response.json())