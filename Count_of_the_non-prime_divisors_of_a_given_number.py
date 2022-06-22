def no(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return True
    else:
        return False
n=int(input())
c=1
for i in range(1,n+1):
    if no(i):
        if(n%i==0):
            c+=1
print(c)