n,h = map(int,input().split())
s = list(map(int,input().split()))
w= 0
for i in range(0,n):
    if s[i]>h : w+=2
    else:w+=1
print(w)