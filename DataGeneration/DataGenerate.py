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
    tablename.append(name)
    cursor.execute("insert into %s values('%d','%f');" %(name, t, open))
db.commit()


cursor = db.cursor()
times = t

while (True):
    time.sleep(1)
    cur_time = time.time()
    for i in tablename:
            b = random.uniform(0.98, 1.02)
            sql = """ select price from %s
                where times = %d;
                """ %(i, times)
            cursor.execute(sql)
            pre_price  = cursor.fetchall()[0][0]
            cur_price = round(pre_price * b, 2)
            cursor.execute("insert into %s values ('%d', '%f'); " %(i, cur_time, cur_price))
            db.commit()
            cursor = db.cursor()
    times = cur_time

# Close connection
db.close()
