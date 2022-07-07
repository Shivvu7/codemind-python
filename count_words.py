s=input()
c=0
if s[0] in 'aeiouAEIOU':
    c=1
for i in range(len(s)-1):
    if (s[i]==' ' and s[i+1] in 'aeiouAEIOU'):
        c+=1
print(c)