
n, k = map(int, input().split())
s = 0
for i in range(1, n + 1):
    s += i * 5
    if s > 240 - k:
        print(i - 1)
        exit()
print(n)
