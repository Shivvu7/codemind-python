n=int(input())
k=0
while(n):
    d=n%10
    if(d>k):
        k=d
    n=n//10
print(k)