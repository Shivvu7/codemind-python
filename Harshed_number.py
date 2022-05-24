def hars(n):
    t=n
    s=0
    while(n):
        d=n%10
        s=s+d
        n=n//10
    if(t%s==0):
        return True
    else:
        return False
n=int(input())
if(hars(n)):
    print('True')
else:
    print('False')