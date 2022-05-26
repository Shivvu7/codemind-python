def prime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
    else:
        return True
n=int(input())
c=0
for i in range(2,n):
    for j in range(2,n):
        if(prime(i)):
            if(prime(j)):
                if(i*j==n):
                    p1=i
                    p2=j
                    c=1
                    break
if(c==1):
    print(p2,p1)
else:
    print("-1")