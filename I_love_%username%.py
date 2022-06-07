input()
s=list(map(int,input().split()))
min = s[0]
max= s[0]
c = 0
for i in s:
    if i > max :
        max = i
        c+=1
        continue
    if i < min :
        min = i
        c+=1
print(c)