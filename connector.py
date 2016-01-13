__author__ = 'onegrx'

import pymssql
from password import secretpassword


class Connector:

    def __init__(self):
        self.server = 'mssql.iisg.agh.edu.pl'
        self.user = 'skala'
        self.db = 'skala_a'

    def connect(self, password):
        conn = pymssql.connect(self.server, self.user, password, self.db)
        conn.autocommit(True)
        return conn

    """ Execue procedure on conn, args has to be tuple of arguments"""
    def execproc(self, conn, procedure, args):
        cursor = conn.cursor()
        cursor.callproc(procedure, args)

    def execquery(self, conn, query):
        cursor = conn.cursor()
        cursor.execute(query)

    def close(self, conn):
        conn.close()






