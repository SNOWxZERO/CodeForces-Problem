t = int(input())
s = [2] * 100
for i in range(1, 101):
    if i & 1:
        s[i - 1] = i + 1
        continue
    s[i - 1] = i - 1
s = list(map(str, s))
for i in range(t):
    n = int(input())
    if n & 1:
        print(' '.join(s[0:n - 3]) + f' {n} {n - 2} {n - 1}')
        continue
    print(' '.join(s[0:n]))
