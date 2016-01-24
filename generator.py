__author__ = 'onegrx'

from connector import Connector
from password import secretpassword
import random

import math

from data_get import *

###############################################


def gen_add_company():

    city, country = getCityCountry()
    company = getCompany()
    login = getLoginCompany(company)
    mail = getMail(company)
    phone = getPhone()
    street = getStreet()
    zipcode = getZip()
    nip = getNip()

    add_company = (company, nip, login, mail, phone, street, city, zipcode, country)

    return add_company


def gen_add_individual():

    name, surname = getNameSurname()
    login = getLoginPersonal(name, surname)
    mail = getMailPersonal(name, surname)
    phone = getPhone()
    street = getStreet()
    city, country = getCityCountry()
    zipcode = getZip()

    add_individual = (name, surname, login, mail, phone, street, city, zipcode, country)

    return add_individual


def gen_add_conference():

    conference = getConference()
    street = getStreet()
    city, country = getCityCountry()
    zipcode = getZip()

    spots = random.randint(4, 30) * 10

    begin, end = getDates()

    price = getPrice()
    discount = '0.5'

    add_conference = (conference, begin, end, street, city, zipcode, country, spots, price, discount)
    return add_conference


def gen_add_thresholds(idconf, i, confday):

    thresholds = [0.4, 0.7, 1]
    (y, m, d) = confday.split("-")
    begin = dt.date(int(y), int(m), int(d)).toordinal()
    # Those dates are rather to than since
    raw_since = [dt.datetime.fromordinal(begin - 90), dt.datetime.fromordinal(begin - 60),
             dt.datetime.fromordinal(begin - 30)]
    since = [(str(date.year), str(date.month), str(date.day)) for date in raw_since]

    result = (str(idconf), str(thresholds[i]), "/".join(since[i]))
    return result


def fill_gen_add_thresholds():
    connector = Connector()
    conn = connector.connect(secretpassword)
    cursor = conn.cursor()
    cursor.execute("select * from conferences")
    row = cursor.fetchone()

    c = Connector()
    cn = c.connect(secretpassword)

    while row:
        idconf = row[0]
        dayofconf = row[2]
        for threshold in range(3):
            res = gen_add_thresholds(idconf, threshold, dayofconf)
            c.apply_proc('AddPrice', res)
            print(res)
        row = cursor.fetchone()
    conn.close()

    cn.close()


def fill_gen_book_places_for_day():
    connector = Connector()
    conn = connector.connect(secretpassword)
    cursor = conn.cursor()
    clients = []
    clients_getter = conn.cursor()
    clients_getter.execute("select clientid from clients")
    clients_ids = clients_getter.fetchone()
    while clients_ids:
        clients.append(clients_ids[0])
        clients_ids = clients_getter.fetchone()

    cursor.execute("select DayId, conferences.DateFrom, Spots "
                   "from DaysOfConf "
                   "inner join Conferences on conferences.ConferenceId = daysofconf.ConferenceId")
    row = cursor.fetchone()

    c = Connector()
    cn = c.connect(secretpassword)


    while row:
        dayid = row[0]
        date = row[1]
        spots_avail = row[2]

        (y, m, d) = date.split("-")
        begin = dt.date(int(y), int(m), int(d)).toordinal()

        for reservation in range(3):
            client = random.choice(clients)
            spots = random.randint(1, int(spots_avail/4))
            book_ord = dt.datetime.fromordinal(begin - random.randint(1, 80))
            date_of_book = "/".join((str(book_ord.year), str(book_ord.month), str(book_ord.day)))
            result = (dayid, client, spots, date_of_book)
            print("Book spots for the day " + str(result))
            c.apply_proc('GeneratorBookPlacesForDay', result)

        row = cursor.fetchone()

    conn.close()
    cn.close()

