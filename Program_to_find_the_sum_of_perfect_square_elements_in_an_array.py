def per(n):
    for i in range(n+1):
        if((i**2)==n):
            return True
n=int(input())
a=list(map(int,input().split()[:n]))
s=0
for i in a:
    if(per(i)):
        s=s+i
print(s)