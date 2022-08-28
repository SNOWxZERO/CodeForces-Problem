n = int(input())
for i in range(142):
    n -= (i * (i + 1) / 2)
    if n > 0:
        continue
    if n == 0:
        print(i)
        break
    print(i - 1)
    break


