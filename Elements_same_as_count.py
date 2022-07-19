n=int(input())
a=list(map(int,input().split()[:n]))
k=[]
for i in a:
    if a.count(i)==i:
        k.append(i)
if len(k)==0:
    print(-1)
else:
    l=[]
    for i in k:
        if i not in l:
            l.append(i)
    print(*l)