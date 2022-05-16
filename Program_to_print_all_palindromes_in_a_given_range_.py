def pal(n):
    s=0
    t=n
    while(n):
        d=n%10
        s=s*10+d
        n=n//10
    if(s==t):
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b):
    if pal(i):
        print(i,end=" ")