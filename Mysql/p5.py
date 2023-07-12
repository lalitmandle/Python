import mysql.connector
myconn = mysql.connector.connect(host = "localhost",user = "root",passwd="lalit",database="ciscobg")

cur=myconn.cursor()

cur.execute("select * from employee")
data = cur.fetchall()

for i in data:
    print(i)
