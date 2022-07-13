n=int(input())
a=list(map(int,input().split()[:n]))
l=[]
for i in a:
    if a.count(i)==i:
        l.append(i)
s=set(l)
if len(s)==0:
    print(-1)
else:
    k=sum(s)/len(s)
    print('%.2f'%k)