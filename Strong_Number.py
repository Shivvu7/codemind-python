def fact(a):
    f=1
    for i in range(1,a+1):
        f=f*i
    return f
n=int(input())
s=0
t=n
while(n):
    d=n%10
    s=s+fact(d)
    n//=10
if(s==t):
    print("The number", t,"is a strong number")
else:
    print("The number",t,"is not a strong number")