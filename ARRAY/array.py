import array as ary1 
# d - decimal values, i -number
ary2 = ary1.array('i',[1,2,3,4,5])
ary3 = ary1.array('d',[1,2,3,4,5])
print(ary2)
print(ary3)
print(type(ary2))
print(ary2[0])
print(ary2[3])
ary4 = ary1.array('u',['a','s','d'])
print(ary4)

#array is mutable - we can change 
arr5 = ary1.array('i',[100,200,300,400])
print(arr5)
arr5[0]=120
arr5[1] = 500
print(arr5)

#scilicing in array
arr6 = ary1.array('i',[1,3,4,5,6,8,9,20])
print(arr6)
#changing first element 
arr6[0] = 0 
print(arr6)

#changing 3rd to 5th element
arr6[2:5] = ary1.array('i',[6,8,25])
print(arr6)

#for add two array
arr7 = arr5+arr6
print("array is joint ===",arr7)