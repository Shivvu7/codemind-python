def prime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
    else:
        return True
n=int(input())
s=0
if(prime(n)):
    while(n):
        d=n%10
        s=s*10+d
        n=n//10
    if(prime(s)):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")