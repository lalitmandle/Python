listnew = list(('sunder','pandian','nellai'))
print(listnew)
l1 = [2,3,4]
l2 = [100,20,30]
l1.extend(l2)
print(l1)

print(l1+l2)
l3 = [2,3,4]
l4 = [45,56,90]

for i in l4:
    l3.append(i)
print(l3)