x=input()
y=input()
s=[]
for i in range(0,len(x)):
    if x[i]==y[i]:
        s.append('0')
    else:s.append('1')
print(''.join(s))