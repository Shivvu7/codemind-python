a,b=map(int, input().split())
d=0
for i in range(1,b):
    if(a%i==0 and b%i==0):
        d=i
print(d)