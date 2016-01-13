__author__ = 'onegrx'
import random


class Company:

    def generate(self):

        with open('data/companies.txt', 'r') as fcompany:
            companies = fcompany.readlines()
            companies = [word.strip() for word in companies]
            company = random.choice(companies)
            return company
