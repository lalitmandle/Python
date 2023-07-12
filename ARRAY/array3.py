A = [[1,2,3,4],
     [-5,6,78,9],
     [-8,9,0,3]]
print(type(A))
print('A = ',A)
print("A[1]= ",A[1])
print("A[1][2]= ",A[1][2])
print("A[0][-1]= ",A[0][-1])

colm = []
for row in A:
    colm.append(row[2])
print('3rd column = ',colm)