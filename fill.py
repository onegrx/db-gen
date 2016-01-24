__author__ = 'onegrx'

from generator import *
from connector import Connector

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


def fill_add_thresholds():
    fill_gen_add_thresholds()


def fill_add_reservations():
    pass



def main():
    fill_add_company()
    fill_add_conference()
    fill_add_thresholds()



main()

