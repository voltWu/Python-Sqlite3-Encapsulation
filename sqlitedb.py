import sqlite3

class sqlitedb:
    __database = ':memory:'
    __conn = sqlite3.connect(__database)

    @staticmethod
    def execute(statement):
        return sqlitedb.__conn.execute(statement)

    @staticmethod
    def close():
        sqlitedb.__conn.close()