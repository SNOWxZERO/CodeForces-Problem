def spliter(DD):
    k = 1
    while DD % 2 == 0:
        k *= 2
        DD /= 2
    return k


t = int(input())
for i in range(t):
    w, h, n = map(int, input().split())
    if n == 1:
        print('YES')
        continue
    if w % 2 != 0:
        if h % 2 != 0:
            print('NO')
            continue
        if spliter(h) >= n:
            print('YES')
            continue
        print('NO')
        continue
    if h % 2 != 0:
        if spliter(w) >= n:
            print('YES')
            continue
        print('NO')
        continue
    if spliter(h) * spliter(w) >= n:
        print('YES')
        continue
    print('NO')