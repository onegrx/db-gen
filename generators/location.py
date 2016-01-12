__author__ = 'onegrx'

import json
import random


class Location:

    def generate(self):
        with open('data/locations.json') as f:
            data = json.load(f)
            country = random.choice(list(data.keys()))
            cities = data[country]
            city = random.choice(cities)
            return city, country

    def show(self):
        print(self.generate())


for i in range(100):
    gen = Location()
    gen.show()
