__author__ = 'onegrx'

import random
import datetime as dt

import generators.location
import generators.credentials
import generators.company
import generators.street
import generators.conference
import generators.person


def getNameSurname():
    personality = generators.person.Person()
    name, surname = personality.generate()
    return name, surname


def getMail(user):
    mail = user[0:5].lower() + "@" + user[0:3].lower() + ".com"
    return mail


def getMailPersonal(n, s):
    return n[0:6].lower() + "@" + s[0:5].lower() + ".com"


def getCompany():
    company_gen = generators.company.Company()
    company = company_gen.generate()
    return company


def getCityCountry():
    location = generators.location.Location()
    city, country = location.generate()
    return city, country


def getLoginCompany(company):
    credentials = generators.credentials.Credentials()
    login = credentials.gen_login_company(company)
    return login


def getLoginPersonal(n, s):
    credentials = generators.credentials.Credentials()
    login = credentials.gen_login_personal(n, s)
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


def getNip():
    nip = random.randint(10**9, 10**10 - 1)
    return str(nip)


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


def getPrice():
    return random.randint(5, 100) * 10