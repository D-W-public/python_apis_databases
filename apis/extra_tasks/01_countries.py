'''
Use the countries API https://restcountries.com/ to fetch information
on your home country and the country you're currently in.

In your python program, parse and compare the data of the two responses:
* Which country has the larger population?
* How much does the area of the two countries differ?
* Print the native name of both countries, as well as their capitals

'''

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
        return f"""{self.country_name.capitalize()}\n{self.native_name}\n\n Capital:\t{self.capital:>10}\n Population:\t{self.population:>10}\n Area:\t\t{self.area:>10} km²\n\n"""

    def compare(self, other):
        if self.population > other.population:
            print(f"{self.country_name.capitalize()} has the larger population.\n")
        elif other.population > self.population:
            print(f"{other.country_name.capitalize()} has the larger population.\n")
        else:
            print(f"{self.country_name.capitalize()}s and {other.country_name.capitalize()}s population are the same size\n")
        
        if self.area > other.area:
            print(f"{self.country_name.capitalize()} is {self.area - other.area} km² bigger than {other.country_name.capitalize()}\n")
        elif other.area > self.area:
            print(f"{other.country_name.capitalize()} is {other.area - self.area} km² bigger than {self.country_name.capitalize()}\n")
        else:
            print(f"{self.country_name.capitalize()} is the same size as {other.country_name.capitalize()}\n")
            


        


if __name__ == '__main__':

    a = Country("austria")
    i = Country("italy")

    print(a, i)    
    a.compare(i)