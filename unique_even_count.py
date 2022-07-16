n=int(input())
a=list(map(int,input().split()[:n]))
k=set(a)
c=0
for i in k:
    if i%2==0:
        c+=1
print(c)