t = int(input())
for i in range(t):
    n = int(input())
    ans = int(n / 3)
    if n % 3 == 0:
        print(f'{ans} {ans}')
        continue
    if n % 3 == 1:
        print(f'{ans + 1} {ans}')
        continue
    print(f'{ans} {ans + 1}')
