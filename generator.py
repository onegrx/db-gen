__author__ = 'onegrx'

from connector import Connector
from password import secretpassword

import random

import generators.location
import generators.credentials
import generators.company
import generators.street


def gen_add_company():
    location = generators.location.Location()
    city, country = location.generate()

    company_gen = generators.company.Company()
    company = company_gen.generate()

    credentials = generators.credentials.Credentials()
    login = credentials.gen_login_company(company)

    mail = company[0:5].lower() + "@" + company[0:3] + ".com"

    range_start = 10**(9-1)
    range_end = (10**9)-1
    phone = random.randint(range_start, range_end)

    street_gen = generators.street.Street()
    street = street_gen.generate()

    zipcode = random.randint(10**4, 10**5 - 1)

    add_company = (company, login, mail, phone, street, city, zipcode, country)

    return add_company

c = Connector()
cn = c.connect(secretpassword)
for i in range(100):
    c.execproc(cn, 'AddCompany', gen_add_company())
c.close(cn)


