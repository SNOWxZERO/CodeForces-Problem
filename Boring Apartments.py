t = int(input())
for i in range(t):
    s = input()
    n = int(s)
    k = len(s)
    if k == 4:
        print((n % 10 - 1) * 10 + 10)
    elif k == 3:
        print((n % 10 - 1) * 10 + 6)
    elif k == 2:
        print((n % 10 - 1) * 10 + 3)
    else:
        print((n % 10 - 1) * 10 + 1)
