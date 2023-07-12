#recursive functions process in 
def f1(n):
    if  n<=1:
        return n
    else:
        return (f1(n-1) + f1(n-2))
n1 = 5
if n1<= 0:
    print("invalide input | please input a positive value")
else:
    print("Fibonacci series:")
for i in range(n1):
    print(f1(i))