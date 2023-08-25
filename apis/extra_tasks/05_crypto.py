'''
https://coinmarketcap.com/api/pricing/
Use the CoinMarketCap API, to repeatedly fetch the price of Bitcoin for a duration of 10 minutes.
Store each value in a dictionary that uses the time of query as a key.

After the script stopped running, determine programmatically at what query time the price
was the highest, and when the lowest.

HINTS:
- You can pick a different API from this list: https://github.com/public-apis/public-apis#cryptocurrency
- You may have to request an API key first. If you need one, remember to include it in your queries.
- You can use packages from the standard library, e.g. for time keeping and dates

BONUS: Explore the `logging` package for easier tracking

'''
import time
import datetime
import requests
from pprint import pprint

url = "https://api.coincap.io/v2/assets/bitcoin"

priceBTC = {}

interval = 10
duration = 600
start_time = datetime.datetime.now()
highest_price = 0.0
highest_timestamp = None
while (datetime.datetime.now() - start_time).total_seconds() < duration:

    response = requests.get(url)
    data = response.json()

    price = data["data"]["priceUsd"]
    price = float(price)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    priceBTC[timestamp] = price

    if price > highest_price:
        highest_price = price
        highest_timestamp = timestamp
    time.sleep(interval)

pprint(priceBTC)

print(f"Highest price: {highest_price} \nTimestamp: {highest_timestamp}")