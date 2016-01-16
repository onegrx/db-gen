__author__ = 'onegrx'

from connector import Connector
from password import secretpassword

import math

from data_get import *

###############################################

def gen_add_company():

    city, country = getCityCountry()
    company = getCompany()
    login = getLogin(company)
    mail = getMail(company)
    phone = getPhone()
    street = getStreet()
    zipcode = getZip()

    add_company = (company, login, mail, phone, street, city, zipcode, country)

    return add_company

def gen_add_conference():

    conference = getConference()
    street = getStreet()
    city, country = getCityCountry()
    zipcode = getZip()

    spots = random.randint(4, 30) * 10

    begin, end = getDates()

    add_conference = (conference, begin, end, street, city, zipcode, country, spots)
    return add_conference

def gen_add_prices(idconf, i, confday, price):

    discount = 0.5
    tresholds = [price * 0.4, price * 0.7, price]
    (y, m, d) = confday.split("-")
    begin = dt.date(int(y), int(m), int(d)).toordinal()
    raw_since = [dt.datetime.fromordinal(begin - 100), dt.datetime.fromordinal(begin - 30),
             dt.datetime.fromordinal(begin)]
    since = [(str(date.year), str(date.month), str(date.day)) for date in raw_since]

    result = (str(idconf), str(math.ceil(tresholds[i])), "/".join(since[i]), str(discount))
    return result

def apply_gen_add_prices():
    connector = Connector()
    conn = connector.connect(secretpassword)
    cursor = conn.cursor()
    cursor.execute("select * from conferences")
    row = cursor.fetchone()

    c = Connector()
    cn = c.connect(secretpassword)

    while row:
        idconf = row[0]
        dayconf = row[2]
        price = random.randint(3, 500) * 10
        for i in range(3):
            res = gen_add_prices(idconf, i, dayconf, price)
            c.execproc(cn, 'AddPrice', res)
            print(res)
        row = cursor.fetchone()
    conn.close()

    c.close(cn)


apply_gen_add_prices()
