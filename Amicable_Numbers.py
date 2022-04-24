a=int(input())
b=int(input())
d=0
s=0
for i in range(1,a):
    if(a%i==0):
        d=d+i
for j in range(1,b):
    if(b%j==0):
        s=s+j
if(s==a and d==b):
    print("Amicable")
else:
    print("Not Amicable")