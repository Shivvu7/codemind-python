def fun(n):
    t=n
    s=0
    while(n):
        d=n%10
        s=s*10+d
        n=n//10
    if s==t:
        return True
    else:
        return False
n=int(input())
c=0
a=list(map(int,input().split()[:n]))
for i in a:
    if fun(i):
        c+=1
print(c)