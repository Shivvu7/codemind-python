s=input()
b=[]
for i in s:
    if i not in b:
        b.append(i)
        
for i in b:
    if i in 'aeiouAEIOU':
        print(i,end=' ')