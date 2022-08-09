t = int(input())
for i in range(t):
    n = int(input())
    s = list(input())
    if n <= 2:
        print('YES')
        continue
    if n == 3:
        if s[0] == s[2] and s[0] != s[1]:
            print('NO')
            continue
        print('YES')
        continue

    temp = s[0]
    s2 = [s[0]]
    for i in s:
        n -= 1
        if i == temp:
            continue
        if i in s2:
            print('NO')
            n = 1
            break
        temp = i
        s2.append(i)

    if n == 0:
        print('YES')
