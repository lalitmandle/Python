dict1 = {'name':'lait','location':'Bangalore','pincode':560103}
print(dict1)
dict1['name']='cisco system'
print(dict1)

dict1['name1'] = 'marathahali'
print(dict1)

dict1.pop('name1')
print(dict1)

dict1.popitem()
print(dict1)
#del dict1 # this will delete the dict
del dict1['location']
print(dict1)

dict2 = dict1.copy()
print(dict2)