# Example for syntex error
try:
    date = eval(input("Enter date: "))
except SyntaxError:
    print("Invalid date entered")
else:
    print("you entered:",date)


#example for IOError
try:
    name = input("Enter filename: ")
    f = open(name,'r')
except IOError:
    print("file not found: ", name)
else:
    n = len(f.readlines())
    print(name, "has ", n, "lines")
    f.close()