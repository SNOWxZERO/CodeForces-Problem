t = int(input())
for i in range(t):
    h, m = map(int, input().split())
    if h == 0:
        print(1380 + (60 - m))
        continue
    if m == 0:
        print((24 - h) * 60)
        continue

    print(((23 - h) * 60) + (60 - m))
