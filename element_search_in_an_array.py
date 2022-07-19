n=int(input())
a=list(map(int,input().split()[:n]))
k=int(input())
c=0
for i in a:
    if i==k:
        c=1
if c==1:
    print(True)
else:
    print(False)