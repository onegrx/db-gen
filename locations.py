__author__ = 'onegrx'

import json
import random


class LocationsGenerator:

    def generate(self):
        with open('data/locations.json') as f:
            data = json.load(f)
            country = random.choice(list(data.keys()))
            cities = data[country]
            city = random.choice(cities)
            print(country + " - " + city)


gen = LocationsGenerator()
for i in range(100):
    gen.generate()
