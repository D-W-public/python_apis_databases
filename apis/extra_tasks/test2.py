import requests

url = "https://api.datamuse.com/words?rel_rhy=apple"

response = requests.get(url)

print(response.json())