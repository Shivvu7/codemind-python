n=int(input())
es, os=0, 0
a=list(map(int, input().split()[:n])) 
for i in range(n):
    if a[i]%2==0:
        es+=a[i]
    else:
        os+=a[i]
if os>es:
    print(os-es)
else:
    print(es-os)