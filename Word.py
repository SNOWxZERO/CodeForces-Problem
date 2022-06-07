s= input()
u=0
d=0
for i in s :
    if i.isupper() : u+=1
    else: d+=1
if d>=u : print(s.lower())
else:print(s.upper())
