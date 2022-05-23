n=int(input())
os=0
es=0
a=list(map(int,input().split()[:n]))
for i in range(n):
    if(i%2==0):
        es+=a[i]
    else:
        os+=a[i]
if(es==os):
    print('YES')
else:
    print("NO")