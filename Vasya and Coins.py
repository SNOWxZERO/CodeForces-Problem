n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a == 0:
        print(1)
    else:
        print(a + b * 2+1)
