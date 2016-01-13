from random import randint

__author__ = 'onegrx'

import subprocess
import sys


class Credentials:

    def gen_password(self):
        password = subprocess.check_output(["openssl", "rand", "-hex", "6"]
                                           ).decode(sys.stdout.encoding).strip()
        return password

    def gen_login_personal(self, name, surname):
        login = name[0:4] + surname[0:6]
        return login.lower() + str(randint(0, 9)) + str(randint(0, 9))

    def gen_login_company(self, companyname):
        login = companyname[0:6]
        return login.lower() + str(randint(0, 9)) + str(randint(0, 9))
