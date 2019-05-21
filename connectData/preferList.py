import pymysql
import time
from connectData import connect

def getuid(username):
    db = connect.connect()
    cursor = db.cursor()
    cursor.execute("use stock_system;")
    cursor.execute("select UID from user where UserName = '%s';" %(username))
    uid = cursor.fetchall()[0][0]
    db.close()
    return uid

def add(username, sid):
    UID = getuid(username)
    SID = sid
    db = connect.connect()
    cursor = db.cursor()
    cursor.execute("use stock_system;")

    cursor.execute("select count(*) from preferlist where SID = '%s' and UID =  '%s';" %(SID,UID))
    count = cursor.fetchall()[0][0]
    if count > 0:
        db.close()
        return
    else:
        cursor.execute("insert into preferlist values('%s', '%s');" %(UID,SID))
        db.commit()
        db.close()
        return

def dele(username, sid):
    UID =getuid(username)
    SID = sid
    db = connect.connect()
    cursor = db.cursor()
    cursor.execute("use stock_system;")
    cursor.execute("delete from preferlist where SID = '%s' and UID =  '%s';" %(SID,UID))
    db.commit()
    db.close()
    return

def req(username):
    UID = getuid(username)
    db = connect.connect()
    cursor = db.cursor()
    cursor.execute("use stock_system;")
    cursor.execute("select SID from preferlist where UID = '%s'; " %(UID))
    d = cursor.fetchall()
    plist ='['
    if d != ():
        for i in d:
            plist = plist +i[0]+','
        plist = plist[:-1] +']'
    return plist
