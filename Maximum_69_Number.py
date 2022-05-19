n=input()
for i in range(len(n)):
    if(n[i]=='6'):
        break
print(n[:i]+'9'+n[i+1:])