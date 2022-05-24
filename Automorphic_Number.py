def auto(n):
    c=0
    a=n*n
    t=n
    while(n):
        d=n%10
        c+=1
        n//=10
    if(a%(10**c)==t):
        return True
    else:
        return False
n=int(input())
if(auto(n)):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")