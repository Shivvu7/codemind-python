n=int(input())
a=list(map(int,input().split()[:n]))
k=[]
for i in a:
    if i not in k:
        k.append(i)
print(*k)