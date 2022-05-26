def prime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
    else:
        return True
a=int(input())
b=int(input())
for j in range(a,b):
    if(j>1):
        if(prime(j)):
            print(j)