a, b = map(int, input().split())
if a > b:
    print(b, int((a - b) / 2))
else:
    print(a, int((b - a) / 2))
