def fun(n):
    t=n
    sc=0
    c=0
    while(n):
        d=n%10
        sc+=1
        if(d!=0):
            if(t%d==0):
                c+=1
        n//=10
    if(sc==c):
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(fun(i)):
        print(i,end=" ")