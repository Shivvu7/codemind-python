n=int(input())
a=list(map(int,input().split()[:n]))
for i in range(n):
    if a[i]%2==1:
        print(a[i],end=' ')
for i in range(n):
    if a[i]%2==0:
        print(a[i],end=' ')