import pymysql
import connect
import random
import time

stockID = ['000001','000002','000003','000004','000005','000006']

t = time.time()
# Connection
db = connect.connect()
cursor = db.cursor()
# Create the database

cursor.execute("use stock_system;")

tablename=[]
for i in stockID:
    open = round(random.uniform(10,100),2)
    name = 'p'+i
    cursor.execute("truncate table %s;" %(name))
db.commit()

db.close()