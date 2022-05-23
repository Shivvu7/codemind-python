n=int(input())
a=list(map(int, input().split()[:n]))
for i in range (n):
    if(a[i]==0):
        print(a[i],end=" ")
for j in range(n):
    if(a[j]==1):
        print(a[j],end=" ")