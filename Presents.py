x = int(input())
s = list(map(int,input().split()))
k = [ 0 for k in range(0,x)]
for i in range(0,x):
    k[s[i]-1] = i+1
print(' '.join(map(str,k)))