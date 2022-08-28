t = int(input())
s = [pow(10, i) for i in range(1, 10)]
for i in range(t):
    ans = 0
    mod = 0
    n = int(input())
    if n < 10:
        print(n)
        continue
    if n in s:
        print((s.index(n) + 1) * 9)
        continue
    for i in s:
        if n > i:
            ans += 9
            continue
        mod = int((s.index(i) + 1) * '1')
        break
    for k in range(1, 10):
        if n >= k * mod:
            ans += 1
            continue
        break
    print(ans)
