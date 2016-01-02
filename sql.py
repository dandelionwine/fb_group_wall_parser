import sqlite3
import sys
import facebook
import requests
import urllib2
import re
from bs4 import BeautifulSoup
from urllib2 import urlopen
import datetime
import time
import xlsxwriter

con = sqlite3.connect('test.db')
cur = con.cursor()


def create_database():
    with con:
        cur.executescript(''' DROP TABLE IF EXISTS Partners;
                CREATE TABLE Partners(id TEXT, name TEXT, link TEXT, free INT, date TEXT, text TEXT);''')
        con.commit()


def add_entry(id, name, link, free, date, text):
    values = [id, name, link, free, date, text]
    cur.execute('INSERT INTO Partners VALUES (?,?,?,?,?,?)', values)
    con.commit()


def get_records():
    a = 0
    cur.execute("SELECT * FROM Partners")
    for i in cur.fetchall():
        print i
        a = a+1
    print a


def set_free(mylink):
    cur.execute('''UPDATE Partners
                SET free = 1
                WHERE link = (?) and free = 2''', (mylink,))


def set_unfree(mylink):
    cur.execute('''UPDATE Partners
                SET free = 0
                WHERE link = (?) and free = 2''', (mylink,))


def get_links():
    cur.execute("SELECT link FROM Partners")
    return cur.fetchall()


def print_database():
    with con:
        cur.executescript("SELECT * FROM Partners")
        for i in (cur.fetchall()):
            print i


def transfer_database():
    workbook = xlsxwriter.Workbook('rsps.xlsx')
    worksheet = workbook.add_worksheet()
    database = cur.execute("SELECT * FROM Partners")
    item = 1
    for i in database:
        worksheet.write("A" + str(item), i[0])
        worksheet.write("B" + str(item), i[1])
        worksheet.write("C" + str(item), i[2])
        worksheet.write("D" + str(item), i[3])
        worksheet.write("E" + str(item), i[4])
        worksheet.write("F" + str(item), i[5])
        item = item + 1
    workbook.close()
