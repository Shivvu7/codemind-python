n=int(input())
a=list(map(int, input().split()[:n]))
s=set(a)
print(*s)