set1 = {1,1,1,2,243,4,5,'sam','jack'}
print(set1)
print(type(set1))

# set.add('usa')

set1.update(['uk','france'])

print(set1)

#we have two methods to delete particular element
#remove and discard -for removing elements
#if there is no element , discard will not throw error
#if there is no element, remove will throw error
set1.remove(1)
print(set1)
set1.discard('sam')
print(set1)

set1.discard('sunder')
print(set1)

# set1.remove("sunder")  #it will show key error
# print(set1)
set2 = {'usa'}


set3 = set(['japan','usa','india'])
set4 = set((1,2,3,4,5))
print(set3)
print(set4)
set3.pop()
print(set3)
set3.clear()
print(set3)
set5 = {'chennai','cochin','delhi'}
print(len(set5))
# set6 = {1,2,3,4}
# del set6
# print(set6)
