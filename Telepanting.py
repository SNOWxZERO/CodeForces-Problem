from bisect import *
n = int(input())
x = [0] * n
y = [0] * n
s = [0] * n
ps = [0] * (n + 1)
for i in range(n):
    x[i], y[i], s[i] = list(map(int, input().split()))
ans = 0

for i in range(n):
    dist = x[i] - y[i]
    j = bisect(x, y[i])
    cost = ps[i] - ps[j]
    dp_i = cost + dist
    ps[i + 1] = ps[i] + dp_i
    ans += s[i] * dp_i
ans += x[-1] + 1
print(ans % 998244353)
'TIME PROBLEM :{ I GIVE UP FOR NOW'
