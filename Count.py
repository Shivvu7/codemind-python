n=int(input())
oc=0
ec=0
a=list(map(int,input().split()[:n]))
for i in range(0,n):
    if(a[i]%2==0):
        ec+=1
    else:
        oc+=1
print(ec,oc,end=" ")