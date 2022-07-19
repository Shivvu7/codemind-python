n=int(input())
a=list(map(int,input().split()[:n]))
avg=sum(a)/n
print("%.2f"%avg)