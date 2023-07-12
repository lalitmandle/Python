#A function to check whether a number is a prime number or composite number
def prime(n):
    """To check if n is prime or not"""
    x = 1 # this will be 0 if not prime 
    for i in range(2,n):
        if n % i == 0:
            x = 0
            break
        else:
            x = 1
    return x
#test if a number is prime or composite 
num = int(input("Enter a number: "))
#check if num is prime or not 
result = prime(num)
if result == 1:
    print(num," is a prime number")
else:
    print(num," is not a prime number")