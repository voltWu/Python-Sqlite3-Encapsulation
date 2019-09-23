import unittest
from sqlitedb import sqlitedb

class MyTestCase(unittest.TestCase):
    def test_sqllitedb(self):
        #create
        cur = sqlitedb.execute("create table if not exists Person(name,age)")
        # Output: -1
        print(cur.rowcount)

        #insert
        cur = sqlitedb.execute("insert into Person(name,age) values('kali',12)")
        assert 1==cur.rowcount and "insert data on table Person failed"

        #update
        cur = sqlitedb.execute("update Person set age = 20 where name = 'kali'")
        assert 1==cur.rowcount and "update data on table Person failed"

        #select
        cur = sqlitedb.execute("select * from Person")
        # Output: ('kali',20)
        for row in cur:
            print(row)

        #delete
        cur = sqlitedb.execute("delete from Person")
        # Output: 1
        print(cur.rowcount)

        #close connection
        sqlitedb.close()


if __name__ == '__main__':
    unittest.main()

