n = int(input())
c = 1
for i in range(2, int(n / 2) + 1):
    if (n - i) % i == 0:
        c += 1
print(c)
