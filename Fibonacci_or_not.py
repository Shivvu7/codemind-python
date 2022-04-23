n=int(input())
n1=0
n2=1
n3=1
c=0
for i in range(0, n):
    n3=n1+n2
    n1=n2
    n2=n3
    if(n==n1):
        c=1
if(c==1):
    print("True")
else:
    print("False")