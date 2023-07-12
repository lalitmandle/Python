import mysql.connector
myconn = mysql.connector.connect(host = "localhost",user = "root",passwd="lalit")
cur=myconn.cursor()
try:
    cur.execute("create database ciscobd")
    dbs = cur.execute("show databases")

except:
    myconn.rollback()
for x in cur:
    print(x)
myconn.close()
