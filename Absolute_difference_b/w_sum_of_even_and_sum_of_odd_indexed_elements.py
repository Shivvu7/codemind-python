n=int(input())
es=0
os=0
a=list(map(int,input().split()[:n]))
for i in range(n):
    if i%2==0:
        es+=a[i]
    else:
        os+=a[i]
if(os>es):
    print(os-es)
else:
    print(es-os)