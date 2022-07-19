n=int(input())
a=list(map(int,input().split()[:n]))
avg=sum(a)//n
c=1
for i in a:
    if avg==i:
        c=2
if c==2:
    print(True)
else:
    print(False)