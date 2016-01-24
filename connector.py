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

    def apply_proc(self, procedure, args):
        conn = self.connect(secretpassword)
        cursor = conn.cursor()
        cursor.callproc(procedure, args)
        conn.close()

    def apply_proc_multi(self, procedure, args, n):
        conn = self.connect(secretpassword)
        cursor = conn.cursor()
        for i in range(n):
            cursor.callproc(procedure, args[i])
            print(procedure + " " + ", ".join(str(v) for v in args[i]))
        conn.close()


    # """ Execue procedure on conn, args has to be tuple of arguments"""
    # def execproc(self, conn, procedure, args):
    #     cursor = conn.cursor()
    #     cursor.callproc(procedure, args)

    # def execquery(self, conn, query):
    #     cursor = conn.cursor()
    #     cursor.execute(query)
    #
    # def fetchdata(self, password):
    #     connection = self.connect(password)
    #     cursor = connection.cursor()
    #     return cursor

