s=input()
c=0
for i in s:
    if ord(i)==32:
        continue
    else:
        c+=1
print(c)