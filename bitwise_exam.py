a = 60 #0011 1100
b = 13 #0000 1101  
print("the bitwise AND operator is ",a&b) # 0000 1100 = 12
print("the bitwise OR operator is ",a | b) # 0011 1101 = 61
print("the bitwise XOR operator is ",a^b) # 0011 0001 = 49

a = 100
b = 50 

print("the bitwise AND operator is ",a&b)
print("the bitwise OR operator is ",a | b)
print("the bitwise XOR operator is ",a^b)

a = 80
b = 90
print("the bitwise AND operator is ",a&b)
print("the bitwise OR operator is ",a | b)
print("the bitwise XOR operator is ",a^b)

"""
~(bitwise NOT) takes one number and inverts all bits of it 
for example a = 60
a =60 = 0011 1100

inverse means output should be 1100 0011 = 195
but python will give -61 
python dosn't support them natively. That means a have an implicit sign attached to them whether you 

to solve this issue do like 
~60 & 255 -this is called as bit mask"""

a=60
print(~a)# output should be 195 but python with give -61
print(~a&255)
print(bin(255))
print(bin(60))