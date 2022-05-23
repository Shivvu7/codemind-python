n=int(input())
o=0
e=0
a=list(map(int, input().split()[:n]))
for i in range(n):
    if(a[i]%2==0):
        e+=1
    else:
        o+=1
print(e,o,end=" ")