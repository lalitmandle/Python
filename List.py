list = [1,2,3,4,5,'sunder',2.3,'2+3j']
print(list)
print(type(list))

print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print(list[5])
print(list[6])
print(list[7])
list[1]='cisco'
print(list)
list.insert(1,"lalit")
print(list)
list.append(200)
print(list)

# list.extend([4,5,6])
# print(list)

# print(len(list))
# #del list , it's delete all list 
# del list[4]
# print(list)

# list.remove('cisco')
# print(list)

print(list[-1])
print(list[:])
print(list[2:5])
print(list[-5:-1])
print(list[::])
print(list[-2:])
print(list[:-3])
print(list[::-1])

list.pop()
print(list)
