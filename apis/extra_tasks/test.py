import requests
from pprint import pprint

class Country:

    def __init__(self, country_name):
        url = f"https://restcountries.com/v3.1/name/{country_name}"
        self.country_name = country_name
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            country_data = data[0]

            self.population = country_data["population"]
            self.area = country_data["area"]
            self.capital = country_data["capital"][0]
            self.native_name = country_data["name"]["nativeName"]
        else:
            print(f"Error: Not able to retriebve data")

    def __str__(self):
        return f"""{self.country_name.capitalize()}\n{self.native_name}\n\n Capital:\t{self.capital:>10}\n Population:\t{self.population:>10}\n Area:\t\t{self.area:>10} km²"""

    def compare(self, other):
        



a = Country("austria")

print(a)