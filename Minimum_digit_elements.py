def fun(n):
    c=0
    while(n):
        d=n%10
        c+=1
        n//=10
    return c
n=int(input())
a=list(map(int,input().split()[:n]))
c=0
k=[]
for i in a:
    k.append(fun(i))
m=min(k)
for i in k:
    print(k.count(m))
    break