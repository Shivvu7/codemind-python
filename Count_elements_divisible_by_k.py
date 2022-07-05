n,a=map(int,input().split())
l=list(map(int,input().split()[:n]))
c=0
for i in range(n):
    if l[i]%a==0:
        c+=1
print(c)