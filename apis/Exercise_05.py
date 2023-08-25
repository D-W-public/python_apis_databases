'''
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

'''

import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.delete(base_url +"/721")
print(response.status_code)

response = requests.get(base_url +"/721")

pprint(response.json())