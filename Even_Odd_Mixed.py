n=int(input())
e=0
c=0
o=0
while(n):
    d=n%10
    c+=1
    if(d%2==0):
        e+=1
    else:
        o+=1
    n=n//10
if(c==e and o==0):
    print("Even")
elif(c==o and e==0):
    print("Odd")
else:
    print("Mixed")