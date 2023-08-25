'''
Using the Chuck Norris API in combination with the datamuse API
( https://api.chucknorris.io/ - https://www.datamuse.com/api/ )

* Query the chucknorris api for a sentence
* Use the last word of that sentence to send a query to the Datamuse API
  and use the rel_rhy (or rel_nry) query parameter to fetch a word that rhymes
* Repeat a coupe of times and store the sentences and rhyme words
* Synthesize the collected results into an avant-garde poem and post on the forum ;)

'''
import requests
from pprint import pprint

def lastWord(string):
  index = string.rfind(" ")
  return string[index+1:-1]

url_1 = "https://api.chucknorris.io/jokes/random"
url_2 = "https://api.datamuse.com/words?rel_rhy="

response = requests.get(url_1)

data = response.json()

print(data["value"])

passed_word = lastWord(data["value"])

response = requests.get(url_2+passed_word)

pprint(response.json())