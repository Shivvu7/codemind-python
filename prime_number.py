n=int(input())
c=0
for i in range(2,n):
    if(n%i)==0:
        c=2
        break
if(c==0):
    print("prime")
else:
    print("not a prime")