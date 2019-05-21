import pymysql
import time
from connectData import connect

def checkexist(username):
    db=connect.connect()
    cursor=db.cursor()
    cursor.execute("use stock_system;")
    cursor.execute("""select count(*) from user where UserName = '%s';""" %(username))
    r = cursor.fetchall()[0][0]
    db.close()
    if r == 0:
        return 0
    else:
        return 1

def checkrepeat(username):
    db=connect.connect()
    cursor=db.cursor()
    cursor.execute("use stock_system;")
    cursor.execute("""select count(*) from user where UserName = '%s';""" %(username))
    r = cursor.fetchall()[0][0]
    db.close()
    if r > 0 :
            return 1
    else:
            return 0

def up(username, password):
    db=connect.connect()
    cursor=db.cursor()
    cursor.execute("use stock_system;")
    cursor.execute("select count(*) from user;")
    num = cursor.fetchall()[0][0]
    id =num+1
    uid = str(id)
    cursor.execute("""insert into user values('%s', '%s', '%s', default);"""%(uid,username,password))
    db.commit()
    db.close()
    return

def logIn(username):
    db=connect.connect()
    cursor=db.cursor()
    cursor.execute("use stock_system;")
    cursor.execute("""select Password from user where UserName ='%s'; """ %(username))
    pw = cursor.fetchall()[0][0]
    db.close()
    return pw

def inState(username):
    db=connect.connect()
    cursor=db.cursor()
    cursor.execute("use stock_system;")
    cursor.execute("""update user set State = 1 where UserName = '%s'; """ %(username))
    db.commit()
    db.close()
    return

def outState(username):
    db=connect.connect()
    cursor=db.cursor()
    cursor.execute("use stock_system;")
    cursor.execute("""update user set State = 0 where UserName = '%s'; """ %(username))
    db.commit()
    db.close()
    return

def reqState(username):
    db=connect.connect()
    cursor=db.cursor()
    cursor.execute("use stock_system;")
    cursor.execute("""select State from user where UserName = '%s'; """ %(username))
    status = cursor.fetchall()[0][0]
    db.close()
    return status
