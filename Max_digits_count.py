def fun(n):
    c=0
    while(n):
        d=n%10
        c+=1
        n//=10
    return c
n=int(input())
a=list(map(int,input().split()[:n]))
k=[]
for i in a:
    b=(fun(i))
    k.append(b)
    c=max(k)
    res=k.count(c)
print(res)