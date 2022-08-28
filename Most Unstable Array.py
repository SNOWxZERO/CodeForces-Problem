t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    if n == 1:
        print(0)
        continue
    if n == 2:
        print(m)
        continue
    print(m*2)