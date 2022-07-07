s=input()
k=input()
c=0
for i in range(len(s)):
    if s[i] in 'aeiouAEIOU':
        if s[i]==k:
            c=1
            z=i
            break
if c==1:
    print("True")
    print(z)
else:
    print("False")
    