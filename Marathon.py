t = int(input())
for i in range(t):
    s = list(map(int, input().split()))
    c = 0
    for i in s:
        if i > s[0]:
            c += 1
    print(c)
