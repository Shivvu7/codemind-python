n=int(input())
while(n):
    a,b=map(int,input().split())
    c=0
    for i in range(a,b+1):
            d=i%10
            if(d==2 or d==3 or d==9):
                c+=1
    print(c)
    n=n-1