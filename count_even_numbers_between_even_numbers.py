n=int(input())
a=list(map(int,input().split()[:n]))
c=0
for i in range(1,n-1,1):
    if a[i-1]%2==0 and a[i+1]%2==0:
       c+=1
print(c)