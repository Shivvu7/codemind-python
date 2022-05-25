n=int(input())
f=1
k=1
for i in range(n):
    a=int(input())
    for j in range(1,a+1):
        f=f*j
    k=f
    f=1
    print(k)