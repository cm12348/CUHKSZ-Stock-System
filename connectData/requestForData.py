import pymysql
import time
from connectData import connect

def getTableName(SID):
    tablename = 'p'+SID
    return tablename

def allData(sid):
    db = connect.connect()
    cursor = db.cursor()
    cursor.execute("use stock_system;")
    name = getTableName(sid)
    cursor.execute(""" select * from %s ;""" %(name))
    all = cursor.fetchall()
    data = ''
    for i in all:
        data = data + str(i[0])+':'+str(i[1])+','
    return data[:-1]

def periodData(timeStart, sid):
    db = connect.connect()
    cursor = db.cursor()
    cursor.execute("use stock_system;")
    name = getTableName(sid)
    cursor.execute("""select * from %s
        where times=%d;""" %(name, timeStart))
    period = cursor.fetchall()
    data = ''
    for i in period:
        data = data + str(i[0])+':'+str(i[1])+','
    return data[:-1]

def stockList():
    db = connect.connect()
    cursor = db.cursor()
    cursor.execute("use stock_system;")
    cursor.execute(""" select * from stock ;""" )
    all = cursor.fetchall()
    data = '['
    for i in all:
        data = data + str(i[0])+','
    data= data[:-1] + ']'
    return data
