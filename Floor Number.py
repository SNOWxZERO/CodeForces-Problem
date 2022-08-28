t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    if n <= 2:
        print(1)
        continue
    if (n - 2) % x != 0:
        print(int((n - 2) / x) + 2)
        continue
    print(int((n - 2) / x) + 1)
