__author__ = 'onegrx'

import random


class Street:

    def generate(self):

        with open('data/streets.txt', 'r') as fstreets:
            streets = fstreets.readlines()
            streets = [word.strip() for word in streets]
            street = random.choice(streets)
            return street
