n = int(input())
s = list(map(int, input().split()))
c = 0
u = 0
for i in range(0, n):
    if s[i] != -1:
        c += s[i]
    else:
        if c == 0:
            u += 1
        else:
            c -= 1

print(u)
