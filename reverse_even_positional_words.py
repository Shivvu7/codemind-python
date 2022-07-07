s=input()
b=s.split()
for i in range(len(b)):
    if i%2==0:
        print(b[i][::-1],end=' ')
    else:
        print(b[i],end=' ')