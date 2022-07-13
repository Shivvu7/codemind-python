n=int(input())
a=list(map(int,input().split()[:n]))
l=[]
for i in a:
    if a.count(i)==i:
        l.append(i)
s=set(l)
print(len(s))