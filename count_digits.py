def fun(n):
    c=0
    if n==0:
        c=1
    if n<0:
        n=abs(n)
    while(n):
        d=n%10
        c+=1
        n//=10
    return c
n=int(input())
a=list(map(int,input().split()[:n]))
for i in a:
   print(fun(i),end=' ')