__author__ = 'onegrx'

from generator import *
from connector import Connector

import time


filler = Connector()
records = 20


"""The first slow version of calling, one connection per one query"""
def fill_add_company_slow():
    for i in range(records):
        proc = 'AddCompany'
        args = gen_add_company()
        print(proc + " " + ", ".join(str(arg) for arg in args))
        filler.apply_proc(proc, args)

"""The second and fast version of calling, one connection for all queries"""
def fill_add_company():
    procedure = 'AddCompany'
    # any other way without i?
    args = [gen_add_company() for i in range(records)]
    filler.apply_proc_multi(procedure, args, records)


def fill_add_individual():
    procedure = 'AddIndividual'
    args = [gen_add_individual() for i in range(records)]
    filler.apply_proc_multi(procedure, args, records)


def fill_add_conference_slow():
    for i in range(records):
        proc = 'AddConference'
        args = gen_add_conference()
        print(proc + " " + ", ".join(str(arg) for arg in args))
        filler.apply_proc(proc, args)


def fill_add_conference():
    procedure = 'AddConference'
    args = [gen_add_conference() for i in range(records)]
    filler.apply_proc_multi(procedure, args, records)


def fill_add_workshop_type():
    procedure = 'AddWorkshopType'
    args = [("How to master your IT skills #" + str(i + 1), ) for i in range(records)]
    filler.apply_proc_multi(procedure, args, records)


def fill_add_thresholds():
    fill_gen_add_thresholds()


def fill_add_reservations():
    fill_gen_book_places_for_day()


def fill_add_attendee():
    fill_gen_add_attendees()


def fill_add_workshop():
    fill_gen_add_workshop()


def fill_add_workshop_reservations():
    fill_gen_book_places_for_workshop()


def fill_add_payment():
    fill_gen_add_payment()


def fill_add_participation():
    fill_gen_assign_attendee()


def main():

    start_time = time.time()

    print("***** Filling Company table *****")
    fill_add_company()

    print("***** Filling Individual table *****")
    fill_add_individual()

    print("***** Filling Conferences table + DaysOfConf by procedure *****")
    fill_add_conference()

    print("***** Filling WorkshopType table *****")
    fill_add_workshop_type()

    print("***** Filling Workshop table *****")
    fill_add_workshop()

    print("***** Filling Prices table *****")
    fill_add_thresholds()

    print("***** Filling Reservations table *****")
    fill_add_reservations()

    print("***** Filling Workshop Reservations table *****")
    fill_add_workshop_reservations()

    print("***** Filling Attendee table with employees + individuals by procedure *****")
    fill_add_attendee()

    print("***** Filling Deposits table *****")
    fill_add_payment()

    fill_add_participation()
    fill_gen_assign_workshop_attendee()

    now = time.time() - start_time

    print("--- %s seconds ---" % now)
    print("--- %s minutes ---" % int(now/60))

main()

