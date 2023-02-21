import csv
import pandas as pd
import os
from sqlalchemy import create_engine
import psycopg2
import PostgreSQL
import datetime
import dateutil
ct = datetime.datetime.now()
print("current time:-", ct)


#Connect local or research databse
conn_string = ''

engine = create_engine(conn_string)
#engine = create_engine('postgresql://postgres:postgres@localhost:5433/newts')

pg_conn = psycopg2.connect(conn_string)
print("Connection ok")
cur = pg_conn.cursor()

#table query
table_sql = '''SELECT table_name
  FROM information_schema.tables
 WHERE table_schema='public'
   AND table_type='BASE TABLE';'''
data = cur.execute(table_sql)
print(data)


table_list = PostgreSQL.list_tables(cur)

for t in table_list:
    table = t[0]
    sql = ''' SELECT count(*) from %s''' % table
    #print(cursor.execute(sql))
    cur.execute(sql)
    data = cur.fetchall()
    print(t[0], "=", data)
