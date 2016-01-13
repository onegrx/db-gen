__author__ = 'onegrx'

from random import randint


class StudentCard:

    def random_with_n_digits(self, n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)

    def generate(self, digits):
        return self.random_with_n_digits(digits)

    def show(self, n):
        print(self.generate(n))

