import re 
str = "welcome to python demo regular expressions python example"
matches = re.findall("python",str)
matchesnew = re.findall("welcome",str)

print(matches)
print("the python occurence",matches)
print(matchesnew)

str1 = "today is 24th march"
mat1 = re.search("\d",str1)
print(mat1)

mat2 = re.search("\w",str1)
print(mat2)

mat3 = re.search("\s",str1)
print(mat3)

str2 = "welcome i am sunder today we are learning regular expression"
mat4 = re.search("sunder",str2)
print(mat4)
print(mat4.string)
print(mat4.group())

str3 = "IT IS very cold today here"
mat5 = re.search("\s",str3)
print(mat5)
print("the first space is available at ",mat5.start())

str4 = " Enter world is in panic"
mat6 = re.split("\s",str4)
print(mat6)
mat7 = re.split("\s",str4,1)
print(mat7)

mat8 = re.split("\s",str4,3)
print(mat8)

#space replace by #,= and $
mat9 = re.sub("\s","#",str4)
print(mat9)
mat10 = re.sub("\s","$",str4)
print(mat10)

str5 = "01234567 Down street"
mat11 = re.findall("[01234]",str5)
print(mat11)
if mat11:
    print("yes the number are available")
else: 
    print("No matching records found")
    