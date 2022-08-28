t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if a == b:
        print(0)
        continue
    if a > b:
        if (a - b) & 1:
            print(2)
            continue
        print(1)
        continue
    if (b - a) & 1:
        print(1)
        continue
    print(2)
