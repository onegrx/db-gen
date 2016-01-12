__author__ = 'onegrx'

import pymssql


class Connector:

    def __init__(self):
        self.server = 'iisg.agh.edu.pl'
        self.user = 'skala'
        self.db = ''


    def conncect(self, password):
        connection = pymssql.connect(self.server, self.user, password, self.db)
        cursor = connection.cursor()
        #cursor.execute()
