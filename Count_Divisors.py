i,r,k=[int(i) for i in input().split()]
c=0
for j in range(i,r+1):
    if(j%k==0):
        c+=1
print(c)