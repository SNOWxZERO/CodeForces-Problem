n = int(input())
s = list(map(int, input().split()))

if len(set(s)) < 3:
    print(0)
else:
    one = []
    two = []
    three = []
    for i in range(0, n):
        if s[i] == 1:
            one.append(i+1)
        elif s[i] == 2:
            two.append(i+1)
        else:
            three.append(i+1)
    MinimumSize = min(len(one), len(two), len(three))
    print(MinimumSize)
    for i in range(MinimumSize) :
        print(f'{one[i]} {two[i]} {three[i]}')

