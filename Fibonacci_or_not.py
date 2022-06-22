n=int(input())
a=0
b=1
c=1
k=0
for i in range(n):
    if(n==a):
        k=1
    a=b
    b=c
    c=a+b
if(k==1):
    print("True")
else:
    print("False")