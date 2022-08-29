n = 0
m = 200005
r = [0] * m
l = [0] * m
s = [0] * m
dp = [0] * m
SUMS = [0] * m
mod = 998244353


def lower_bound(v):
    l = 1
    ri = n
    ans = 0
    while ri >= l:
        mid = l + ri >> 1
        if r[mid] >= v:
            ri = mid - 1
            ans = mid
        else:
            l = mid + 1
    return ans


n = int(input())
for i in range(1, n + 1):
    r[i], l[i], s[i] = map(int, input().split())
ans = 0
for i in range(1, n + 1):
    ans = (ans + r[i] - r[i - 1]) % mod
    p = lower_bound(l[i]) - 1
    dp[i] = (r[i] - l[i] + SUMS[i - 1] - SUMS[p] + mod * 2) % mod
    SUMS[i] = (SUMS[i - 1] + dp[i]) % mod
    if s[i]: ans = (ans + dp[i]) % mod
print((ans + 1) % mod)
