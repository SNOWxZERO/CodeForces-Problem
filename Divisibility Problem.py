n = int(input())
for i in range(0, n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a <= b:
        print(b - a)
    else:
        if a % b != 0:
            print(((int(a / b) + 1) * b) - a)
        else:
            print(0)
