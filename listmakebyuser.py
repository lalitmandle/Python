A = [1,2,3,4,5,6,7,8,9,10]
print(A)
sum1 = sum(A)
print(sum1)
avg = sum1/10
print(avg)

a = []
n = int(input("Enter the number of elements in list: "))
for i in range(0,n):
    element = int(input("Enter element "+str(i + 1)+":"))
    a.append(element)
temp = a[0]
a[0]=a[n-1]
a[n-1] = temp
print('New list is : ')
print(a)