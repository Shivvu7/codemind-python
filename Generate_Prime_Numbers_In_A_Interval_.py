def p(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
a=int(input())
b=int(input())
for i in range(a,b+1):
    if p(i):
        if(i!=1):
            print(i)