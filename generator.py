__author__ = 'onegrx'

from connector import Connector
from password import secretpassword

import random
import datetime as dt
import math

import generators.location
import generators.credentials
import generators.company
import generators.street
import generators.conference

def getCompany():
    company_gen = generators.company.Company()
    company = company_gen.generate()
    return company

def getCityCountry():
    location = generators.location.Location()
    city, country = location.generate()
    return city, country

def getLogin(company):
    credentials = generators.credentials.Credentials()
    login = credentials.gen_login_company(company)
    return login

def getPhone():
    range_start = 10**(9-1)
    range_end = (10**9)-1
    phone = random.randint(range_start, range_end)
    return phone

def getStreet():
    street_gen = generators.street.Street()
    street = street_gen.generate()
    return street

def getZip():
    zipcode = random.randint(10**4, 10**5 - 1)
    return zipcode

def getConference():
    conference_gen = generators.conference.Conference()
    conference = conference_gen.generate()
    return conference

def getDates():
    currentdate = dt.datetime.now()
    begin = currentdate.toordinal() + random.randint(1, 400)
    end = begin + random.randint(0, 5)
    begin = dt.date.fromordinal(begin)
    end = dt.date.fromordinal(end)
    start = (str(begin.year), str(begin.month), str(begin.day))
    end = (str(end.year), str(end.month), str(end.day))
    return "/".join(start), "/".join(end)

###############################################

def gen_add_company():

    city, country = getCityCountry()
    company = getCompany()
    login = getLogin(company)
    mail = company[0:5].lower() + "@" + company[0:3] + ".com"
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
