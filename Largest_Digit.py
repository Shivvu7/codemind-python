n=int(input())
t=0
while(n):
    d=n%10
    if(d>t):
        t=d
    n//=10
print(t)