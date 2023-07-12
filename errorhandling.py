# try:
#     a = int(input("enter a "))
#     b = int(input("enter b "))
#     c = a/b
#     print("the value of c is: ",c)

# except ZeroDivisionError:
#     print("Infinity")

# except ValueError:
#     print("Wrong input given \n")

# try:
#     d = int(input("Enter the d: "))
#     e = int(input("enter the e: "))
#     print(d)
#     print(e)
# except ValueError:
#     print("\nwronge inputs entered")
# finally:
#     print("data is cleaned\n")


# try:
#     list1 = [110,23,432,4]
#     print(list1[10])
# except LookupError:
#     print("\ninput out of range")

# try:
#     dict1 = {"name":"channai","state":"tamilnadu"}
#     print(dict1['country'])
# except KeyError:
#     print("key/value not existing")

# try:
#     import math
#     print(math.exp(10000))
# except OverflowError:
#     print("Overflow values")
# else:
#     print("success ")

# try:
#     x = int(input("enter a \n"))
#     y = int(input("enter b \n"))

#     assert x== y
# except AssertionError:
#     print("assertion error")

# else:
#     print("success both are same ")

import sys
while True:
    try:
        a = int(input("enter an integer: "))
        r = 1/a
        break

    except:
        print("the error is ",sys.exc_info()[0],"occured")
        print("p1 try again")
        print()
print("the value is ",r)