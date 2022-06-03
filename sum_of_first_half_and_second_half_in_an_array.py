n=int(input())
a=list(map(int,input().split()))
s,k=0,0
for i in range(0,(n//2)):
    s=s+a[i]
for i in range(n-1,(n//2)-1,-1):
    k=k+a[i]
print(s)
print(k)