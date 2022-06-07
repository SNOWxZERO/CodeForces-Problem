n,t = map(int,input().split())
s= input()
s1 = ['' for k in range(0,n)]
for j in range(0,t):
    i=0
    while(i<n):
        if i == n-1 :
            s1[i] = s[i]
            break
        if s[i] == 'B' and s[i+1]=='G':
            s1[i]='G'
            s1[i+1]='B'
            i+=2
        else:
            s1[i]=s[i]
            i+=1
    s=''.join(s1)
print(s)