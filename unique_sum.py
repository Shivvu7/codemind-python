n=int(input())
a=list(map(int,input().split()[:n]))
k=set(a)
c=0
for i in k:
    c+=i
print(c)