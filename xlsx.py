import xlsxwriter
import sql
import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()
database = cur.execute("SELECT * FROM Partners")

def create_excel():
    workbook = xlsxwriter.Workbook('rsps.xlsx')
    worksheet = workbook.add_worksheet()

def transfer_database():
    item = 1
    for i in sql.database:
        worksheet.write("A" + str(item), i[0])
        worksheet.write("B" + str(item), i[1])
        worksheet.write("C" + str(item), i[2])
        worksheet.write("D" + str(item), i[3])
        item = item + 1
    workbook.close()


