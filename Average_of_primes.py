def fun(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
a=list(map(int,input().split()[:n]))
c=s=0
for i in range(n):
    if fun(a[i]) and a[i]>1:
            s+=a[i]
            c+=1
k=s/c
print("%.2f"%k)