n=int(input())
a=list(map(int,input().split()[:n]))
c=0
k=[]
for i in a:
    if a.count(i)==i:
        k.append(i)
s=set(k)
for i in s:
    c+=1
print(c)
