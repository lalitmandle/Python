import datetime
now = datetime.datetime.now()
print(now)
now1 = datetime.date.today()
print(now1)
print(now1.year)
print(now1.month)

print(now1.strftime('%Y'))
print(now1.strftime('%y'))
print(now1.strftime('%M'))
print(now1.strftime('%m'))
print(now1.strftime('%S'))

