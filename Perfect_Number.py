b=int(input())
s=0
for i in range(1,b):
    if(b%i)==0:
        s+=i
if(s==b):
    print("True")
else:
    print("False")