rows = int(input("enter the value of row \n"))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end= " ")
    print()

n = 5

for i in range(1,n):
    for j in range(i):
        print("$",end=" ")
    print(" ")

# pattern for number 
def pattern(n):
    x = 0
    for i in range(0,n):
        x += 1
        for j in range(0,i+1):
            print(x,end=" ")
        print(" ")
pattern(4)

for i in range(5):
    for j in range(5):
        if i+j ==2 or i-j ==2 or i + j == 6 or j-i ==2:
            print("*",end="")
        else:
            print(end = " ")
        print()
        