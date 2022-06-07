n=int(input())
s=[[0,0] for k in range(0,n)]
c=0
for i in range(0,n):
    s[i]=list(map(int,input().split()))
for l in range(0,n):
    for j in range(0,n):
        if l==j : continue
        if s[l][0]==s[j][1] : c+=1
print(c)