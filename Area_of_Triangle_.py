a,b,c=[int(x) for x in input().split()]
s=(a+b+c)/2
v=s*(s-a)*(s-b)*(s-c)
k=pow(v,0.5)
print("%.2f"%k)