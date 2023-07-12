l1=[1,2,3,4]
l2=['one','two','three']
l3=[1,2,3,4,'sundar','tandam','caddcae']
print(l1)
print(l2)
print(l3)
print(type(l1))
print(type(l2))
print(type(l3))
print(l1[0])#postive indexing starts from zero
print(l2[2])
print(l3[4])
print(l1[-1]) #negative indexing starts from -1
print(l2[-3])
print(l3[-4])
#index slicing
print(l1[1:3])
print(l1[0:3])
print(l3[2:])
print(l1[:])
print(l2[:])
print(l3[:])
print(l3[-5:-1])
print(l2[-3:-1])

list1 = ['india','usa','japan']
list2 = ['pak','uk']
list3 = list1+list2
print(list3)
list4 = ['tandam','caddce']
list5 = list4.copy()
print(list5)
list6 = [1,2,3,4,90]
list6.clear()
print(list6)

listy= [1,2,3]
listy.append(1000)
print(listy)
listy.extend([2000,3000])
print(listy)
print(['lalit']*4)