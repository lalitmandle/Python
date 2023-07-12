def Reverse_Integer(Num):
    Reverse = 0
    while(Num>0):
        Reminder = Num%10
        Reverse = (Reverse*10)+Reminder
        Num = Num//10
    return Reverse
Num= int(input("Please Enter any Number: "))
Reverse = Reverse_Integer(Num)
print("\nReverse of entered number is = %d"%Reverse)
