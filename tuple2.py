tup1 = (1,2,3,4,5,6)
tup2 = (3,4,5,6)
tup3= tup1+tup2
print(tup3)

# del tup3
# print(tup3)

tup3 = ("carrot","brinjal","cabbage")
print(len(tup3))
tup4 = tuple((1,2,3,4))
print(tup4)
# if we want to modify tuple the only option is convert into a list
tup5 = list(tup4)
print(tup5)
tup5[2]='ca'
print(tup5)
tup0 = ('cricket','football','hockey','tennis')
for i in tup0:
    print(i)
if 'cricket' in tup0:
    print("yes")

tup1 = tuple(input('enter elements in a tuple in run time===  '))
print(tup1)
count = 0
for i in tup1:
    print('tuple[%d] =%s' %(count,i))
    count = count+1
