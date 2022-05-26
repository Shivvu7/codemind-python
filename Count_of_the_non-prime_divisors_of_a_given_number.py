def nonprime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return True
    else:
        return False
n=int(input())
c=1
for j in range(1,n+1):
    if(n%j==0):
        if(nonprime(j)):
            c+=1
print(c)