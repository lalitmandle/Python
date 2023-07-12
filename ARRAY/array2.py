import array as ary
ary1 = ary.array('i',[])
n= int(input("Enter number of elements : "))
for i in range(0,n):
    ele = int(input("enter the values of array:  "))
    ary1.append(ele)
print(ary1)
print(type(ary1))