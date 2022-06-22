s=0
n=int(input())
while(n):
    d=n%10
    s=s*10+d
    n=n//10
print(s)