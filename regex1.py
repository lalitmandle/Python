import re 
str = "we are into new era of python learning"
mat1 = re.search("new",str)
print(type(mat1))
print(mat1.span())
print(mat1)