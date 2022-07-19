n=int(input())
a=list(map(int,input().split()[:n]))
k=a[::-1]
c=0
for i in range(n):
    c+=k[i]*(2**i)
print(c)