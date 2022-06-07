n = input()
count = 0
for i in range(0, len(n)):
    if n[i]=='7'or n[i]=='4' :
        count+=1
if count == 7 or count==4 :
    print('YES')
else:print("NO")