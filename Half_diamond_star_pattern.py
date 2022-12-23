n=int(input())
if(n<=100 and n>=3):
    for i in range(1,n+1):
        for j in range(i):
            print('*',end='')
        print()
    for i in range(n-1,0,-1):
        for j in range(i):
            print('*',end='')
        print()
else:
    print('The pattern is not possible')