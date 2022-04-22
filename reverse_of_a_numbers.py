n=int(input())
s=0
while(n):
    d=n%10
    s=s*10+d
    n=n//10
print(s)