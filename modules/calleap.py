import calender 
if (calender.isleap(2020)):
    print("The year is leap")
else:
    print("The year is not leap")

print("The leap days between 2000 and 2040 are : ",end = '')
print(calender.leapdays(2000,2040))