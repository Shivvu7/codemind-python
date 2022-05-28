def even(n):
    c=0
    while(n):
        d=n%10
        c+=1
        n//=10
    return c
n=int(input())
a=list(map(int,input().split()[:n]))
k=0
for i in a:
    if even(i)%2==0:
        k+=1
print(k)