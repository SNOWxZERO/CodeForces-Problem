x= int(input())
s=''
for i in range(0,x):
    if i%2==0:
        s+='I hate '
    else:s+='I love '
    if i ==x-1:
        s+='it '
    else:s+='that '
print(s)

