import mysql.connector
myconn = mysql.connector.connect(host = "localhost",user = "root",passwd="lalit",database="ciscobg")
cur=myconn.cursor()
try:
    dbs = cur.execute("create table employee(name varchar(20) not null,id int not null)")
    print("table created successfully")
    
except:
    myconn.rollback()

myconn.close()
