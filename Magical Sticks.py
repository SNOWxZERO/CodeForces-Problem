t = int(input())
for i in range(t):
    n = int(input())
    if n < 3:
        print(1)
        continue
    if n % 2 == 0:
        print(int(n / 2))
        continue
    print(int((n / 2)+1) )
