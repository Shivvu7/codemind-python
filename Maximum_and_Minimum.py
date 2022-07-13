n=int(input())
a=list(map(int,input().split()[:n]))
l=[]
for i in a:
    if a.count(i)==i:
        l.append(i)
if len(l)==0:
    print(-1)
else:
    print(min(l),max(l))