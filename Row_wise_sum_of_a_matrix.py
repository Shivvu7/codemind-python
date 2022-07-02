a,b=map(int,input().split())
for i in range(a):
    l=list(map(int,input().split()[:b]))
    s=0
    for i in l:
        s+=i
    print(s,end=" ")