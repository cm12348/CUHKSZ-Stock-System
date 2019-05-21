import pymysql
def connect():
    db = pymysql.connect("localhost", "root","")
    return db
