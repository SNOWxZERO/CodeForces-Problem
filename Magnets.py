n= int(input())
k=' '
c=1
for i in range(0,n):
    s= input()
    if( s == '01' and k =='-') or (s=='10' and k=='+'):
        c+=1
    if s=='01':
        k='+'
    else:k='-'
print(c)

