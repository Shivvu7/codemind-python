a=int(input())
s=0
n=a*a
while(n):
    d=n%10
    s=s+d
    n=n//10
if(s==a):
    print("Neon Number")
else:
    print("Not Neon Number")