n=int(input())
s=[]
for i in range(n):
    x=int(input())
    if x%2==0 : s.append(str(int(x/2)-1))
    else:s.append(str(int(x/2)))
print('\n'.join(s))