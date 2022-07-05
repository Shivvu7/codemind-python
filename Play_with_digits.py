def fun(n):
    s=0
    while(n):
        d=n%10
        s=s+d
        n//=10
    return s
n=int(input())
k=0
l=list(map(int,input().split()[:n]))
for i in l:
    k=k+fun(i)
print(k)