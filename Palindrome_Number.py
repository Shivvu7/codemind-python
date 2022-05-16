def pal(n):
    s=0
    t=n
    while(n):
        d=n%10
        s=s*10+d
        n=n//10
    if(s==t):
        return True
    else:
        return False
k=int(input())
while(k):
    a=int(input())
    if(pal(a)):
        print("True") 
    else:
        print("False")