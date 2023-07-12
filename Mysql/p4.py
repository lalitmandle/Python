import mysql.connector
myconn = mysql.connector.connect(host = "localhost",user = "root",passwd="lalit",database="ciscobg")

cur=myconn.cursor()

sql = "insert into employee(name,id) values(%s,%s)"
val = ("arthy",1)

try:
    cur.excute(sql,val)
    myconn.commit()
    
except:
    myconn.rollback()

print("one record inserted")
myconn.close()
