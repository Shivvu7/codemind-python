s=input()
c=s[::-1]
if s.count(' ')==0:
    print(s[0])
for i in range(1,len(c)):
    if c[i] ==' ':
        print(c[i-1])
        break