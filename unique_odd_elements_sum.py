n=int(input())
a=list(map(int,input().split()[:n]))
s=set(a)
c=0
for i in s:
    if i%2==1:
        c+=i
print(c)