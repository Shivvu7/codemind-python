n=int(input())
a=list(map(int,input().split()[:n]))
c=0
s=set(a)
for i in s:
    if i%2==1:
        c+=1
print(c)