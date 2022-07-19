n=int(input())
a=list(map(int,input().split()[:n]))
c=k=0
for i in range(n):
    if a[i]%2==0 and i%2==0:
        c+=1
    if a[i]%2==0:
        k+=1
        
if c==k:
    print(True)
else:
    print(False)