#nesting of dictionaries
dict1 = {
    "courses":{'name':'python','topic':'collection'},
    "courses1":{'name':'java','topic':'databses'},
    "courses2":{'name':'c','topic':'pointer'},
    "courses3":{'name':'c++','topic':'oops'},
}
print(dict1)

new = ('sunder','python','tuplewithdictexample')
new1 = 0
dictnew = dict.fromkeys(new,new1)
print(dictnew)

dictnew1 = dict.fromkeys(new)
print(dictnew1)


dict2 = {'name':'sunder','course':'datascience','duration':30}
print(dict2)
print(type(dict2))
dict2['topic'] = 'dictionary'
print(dict2)
for i in dict2.items():
    print(i)
for j in dict2.values():
    print(j)
