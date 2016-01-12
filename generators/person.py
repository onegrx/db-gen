__author__ = 'onegrx'

import random

class Person:

    def generate(self):

        with open('data/names.txt', 'r') as fnames:
            names = fnames.readlines()
            names = [word.strip() for word in names]
            name = random.choice(names)

        with open('data/surnames.txt', 'r') as fsurnames:
            surnames = fsurnames.readlines()
            surnames = [word.strip() for word in surnames]
            surname = random.choice(surnames)

        return name, surname

    def show(self):
        print(self.generate())

for i in range(20):
    gen = Person()
    gen.show()