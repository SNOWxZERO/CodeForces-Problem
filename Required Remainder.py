t = int(input())
for i in range(0, t):
    x, y, n = list(map(int, input().split()))
    if n < x:
        print(y)
        continue
    m = n % x
    if m == y:
        print(n)
        continue
    if m > y:
        print(n - (m - y))
        continue
    print(n - m - (x - y))
