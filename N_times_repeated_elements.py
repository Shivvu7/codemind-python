n=int(input())
a=list(map(int,input().split()[:n]))
k=int(input())
c=0
s=[]
for i in a:
    if a.count(i)==k:
        s.append(i)
if len(s)==0:
    print(-1)
else:
    print(*set(s))