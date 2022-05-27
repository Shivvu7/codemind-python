n=int(input())
a=list(map(int,input().split()[:n]))
c=[]
k=[]
for i in a:
    c.append(i*i)
    k=sorted(c)
print(*k)