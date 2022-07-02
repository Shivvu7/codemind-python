a,b=map(int,input().split())
s=0
for i in range(a):
    a=list(map(int,input().split()[:b]))
    for k in a:
        s+=k
print(s)