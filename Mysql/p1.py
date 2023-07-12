import mysql.connector
myconn = mysql.connector.connect(host = "localhost",user = "root",passwd="lalit")
print(myconn)

print("python with msql connected successfully")
