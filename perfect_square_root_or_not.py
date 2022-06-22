n=int(input())
c=0
for i in range(1,int(n**0.5)+1):
    if(i==(n**0.5)):
        c=1
if(c==1):
    print("True")
else:
    print("False")