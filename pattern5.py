lines = 4
i = 1
j = 1
while i <= lines:#this loop is used to print lines
    j = 1
    while j<=lines:
        if i == j:
            print("*",end=" ")
        else:
            print("0",end=" ")
        j = j+1
    j = j-1
    print("*",end=" ")
    while j>=1:
        if i == j:
            print("*",end=" ")
        else:
            print("0",end=" ")
        j = j-1
    print("")
    i = i+1