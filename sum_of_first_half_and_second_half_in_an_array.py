n=int(input())
a=list(map(int,input().split()[:n]))
c=n//2
s=a[:c:]
k=a[c::]
print(sum(s))
print(sum(k))