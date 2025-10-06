#calculate the factorial(using while loop)
n=int(input("enter a number"))
a=1
while n>0:
    a*=n
    n-=1
print(a)
