x,y=[int(x) for x in input().split()]
d=1
l=1
for i in range(1,y):
    if(x%i==0 and y%i==0):
        d=i
l=x*y//d
print(l)