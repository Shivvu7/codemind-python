a=int(input())
c=0
for i in range (1, a):
    if(a==i*(i+1)):
        c=1
if(c==1):
    print("YES")
else:
    print("NO")