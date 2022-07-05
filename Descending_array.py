n=int(input())
l=list(map(int,input().split()[:n]))
c=sorted(l)[::-1]
if c==l:
    print("yes")
else:
    print("no")