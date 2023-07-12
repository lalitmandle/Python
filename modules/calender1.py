from datetime import date
import calender

date1 = date(2023,3,20)
date2 = date(2023,2,19)
diff = date1-date2
print(diff.days)

print("The calender of the year 2020 is :")
print(calender.calendar(2020,2,1,6))
print(calender.calendar(2020,1,1,6))

#using firstweekday() to print starting day number 
print("The starting day number in calender is : ",end = ' ')
print(calender.firstweekday())
