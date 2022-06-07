n=int(input())
s=list(map(int,input().split()))
m=0
for i in range(0,n):
    m+=s[i]
print(m/n)