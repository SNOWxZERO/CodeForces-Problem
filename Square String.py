t = int(input())
for i in range(t):
    s = list(input())
    n = len(s)
    if n & 1:
        print('NO')
        continue
    s1 = s[:int(n / 2)]
    s2 = s[int(n / 2):]
    if s1 == s2:
        print('YES')
        continue
    print('NO')
