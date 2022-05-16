t=int(input())

while t:
    a=int(input())
    c=0
    for i in range(0,a):
        if(i*i==a):
            c+=1
    if (c>0):
        print("True")
    else:
        print("False")