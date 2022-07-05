n=int(input())
l=list(map(int,input().split()[:n]))
c=set(l)
if sorted(c)==l:
    print("yes")
else:
    print("no")