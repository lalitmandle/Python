import time
import datetime
import calender
print(time.asctime(time.localtime(time.time())))
print(datetime.datetime.now())
print(time.localtime)
print(datetime.datetime(2020,6,10))
print(datetime.datetime(2020,6,10,14,15,10))
calender.rcal(2020)
x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))

print(x.year)
print(x.strftime("%a"))

x = datetime.datetime(2018,6,1)
print(x.strftime("%B"))
x = datetime.datetime(2018,6,1)
print(x.strftime("%b"))