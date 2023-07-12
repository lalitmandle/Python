import calendar
call = calendar.month(2023,3)
print(call)
call2 = calendar.prcal(2023)
print(call2)
call3=  calendar.TextCalendar(calendar.SUNDAY).formatyear(2023)
print(call3)
# Enter the month and year
yy = int(input("Enter year : "))
mm = int(input("Enter month:  "))
# display the calender
print(calendar.month(yy,mm))