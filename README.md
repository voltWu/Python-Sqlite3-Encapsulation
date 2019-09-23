# Introduction

SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language. and it's the most used database engine in the world. *Python* supported SQLite at *Python3* version. *Python3* has a build-in module `sqlite3`. 

# Environment
Python: Python3.6

# Settings

The only thing you need to configure that is the `__database` in *sqlitedb.py*. it is a *file-liked* object that which used to store data permanently. or `:memory:` if you want only to store data at RAM(random access memory).

## store data permanently
```PYTHON
__database = 'mydb.db'
```
the file *mydb.db* will be created if not exists before. the *mydb.db* can be shared at multiple session.

## store data temporarily
```PYTHON
__database = ':memory:'
```
the data will be store temporarily at Random Access Memory. the data will be wiped when application exit.

# How to use sqlitedb class

The class `sqlitedb` has two static methods. `execute` and `close`. the function `execute` used to execute SQL statement, and `close` used to close connection and release resource.
```PYTHON
#import sqlitedb class from sqlitedb module
from sqlitedb import sqlitedb

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
```

don't forget to close when don't need connection anymore.

# Reference

About how to use sqlite3 at [python sqlite3 module](https://docs.python.org/3.6/library/sqlite3.html?module-sqlite3).

About how to use sqlite at [sqlite document](https://www.sqlite.org/index.html)
