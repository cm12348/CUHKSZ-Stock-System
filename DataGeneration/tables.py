import pymysql
import connect


stockID = ['000001','000002','000003','000004','000005' ,'000006']

db = connect.connect()
cursor= db.cursor()
cursor.execute("create Database stock_system;")
cursor.execute("use stock_system;")
sql = """create table user(
    UID char(8) Not Null,
    UserName varchar(10) Not Null,
    Password varchar(20) Not Null,
    State boolean Default 0,
    Primary key (UID)
    );
    """

cursor.execute(sql)
sql = """ create table stock(
    SID char(6) not null,
    primary key (SID)
    );"""
cursor.execute(sql)

sql = """create table preferlist(
    UID char(8) Not Null,
    SID char(6) Not Null,
    primary key (UID, SID),
    FOREIGN KEY (UID) REFERENCES user(UID),
    FOREIGN KEY (SID) REFERENCES stock(SID)
    );"""
cursor.execute(sql)

tablename=[]
for i in stockID:
    name = 'p'+i
    tablename.append(name)
    cursor.execute("insert into stock values('%s');" %(i))
db.commit()

cursor=db.cursor()
for i in tablename:
    sql = """CREATE TABLE %s
        (
        times int Not Null,
        price double Not Null
        );
    """ %(i)
    cursor.execute(sql)


db.close()
