def fun(n):
    s=0
    while(n):
        d=n%10
        s=s*10+d
        n=n//10
    return s
n=int(input())
a=list(map(int,input().split()[:n]))
for i in a:
    print(fun(i),end=" ")