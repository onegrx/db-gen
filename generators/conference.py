__author__ = 'onegrx'
import random


class Conference:

    def generate(self):

        with open('data/conferences.txt', 'r') as fconferences:
            conferences = fconferences.readlines()
            conferences = [word.strip() for word in conferences]
            conference = random.choice(conferences)
            return conference
