__author__ = 'onegrx'

import pymssql


class Connector:

    def __init__(self):
        self.server = 'mssql.iisg.agh.edu.pl'
        self.user = 'skala'
        self.db = 'skala_a'

    def connect(self, password):
        conn = pymssql.connect(self.server, self.user, password, self.db)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM information_schema.tables")

        for row in cursor:
            print('row = %r' % (row,))

        conn.close()

c = Connector()
c.connect("")
