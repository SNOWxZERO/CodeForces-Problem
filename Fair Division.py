t = int(input())

for i in range(t):

    n = int(input())
    s = list(map(int, input().split()))
    sum1 = sum(s)
    if n == 1:
        print('NO')
        continue
    if sum1 % 2 != 0:
        print('NO')
        continue
    c1 = s.count(1)
    if (sum1 / 2) % 2 == 0:
        print('YES')
        continue
    if c1 > 0:
        print('YES')
        continue
    print('NO')
