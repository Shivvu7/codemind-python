n=int(input())
a=list(map(int, input().split()[:n]))
c=0
for i in range(n):
    c+=a[i]
print(c)