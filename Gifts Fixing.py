t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    ma = min(a)
    mb = min(b)
    for i in range(n):
        ans += max(a[i] - ma, b[i] - mb)

    print(ans)
