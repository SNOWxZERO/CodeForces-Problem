t = int(input())
ce = 0
co = 0
for i in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(0, n, 2):
        if a[i] % 2 != 0:
            ce += 1
    for i in range(1, n , 2):
        if a[i] % 2 == 0:
            co += 1

    if ce == 0 and co == 0:
        print(0)
    elif ce - co == 0:
        print(ce)
    else:
        print(-1)
    ce = 0
    co = 0
