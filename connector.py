__author__ = 'onegrx'

import pymssql


class Connector:

    def __init__(self):
        self.server = 'mssql.iisg.agh.edu.pl'
        self.user = 'skala'
        self.db = ''

    def connect(self, password):
        conn = pymssql.connect(self.server, self.user, password)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM master.dbo.sysdatabases")

        for row in cursor:
            print('row = %r' % (row,))

        conn.close()

c = Connector()
c.connect("password")
