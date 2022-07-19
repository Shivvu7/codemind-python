n=int(input())
a=list(map(int,input().split()[:n]))
avg=sum(a)//n
c=0
for i in range(n):
    if a[i]<=avg:
        c+=1
print(c)