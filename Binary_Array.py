n=int(input())
c=k=0
a=list(map(int,input().split()[:n]))
for i in a:
    if i==1:
        c+=1
    if i==0:
        k+=1
if c+k==n:
    print(True)
else:
    print(False)