s=list(map(int,input().split()))
c=0
s.sort()
for i in range(0,3) :
    if s[i]==s[i+1]:
        c+=1

print(c)