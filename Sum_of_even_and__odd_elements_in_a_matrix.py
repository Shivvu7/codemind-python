a,b=map(int,input().split())
s=k=0
for i in range(a):
    l=list(map(int,input().split()[:b]))
    for i in l:
        if i%2==0:
            s+=i
        else:
            k+=i
print(s,k)