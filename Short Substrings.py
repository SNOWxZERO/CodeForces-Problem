n = int(input())
s = []
for i in range(n):
    x = input()
    s.append([])
    for j in range(0, len(x) - 1,2):
        s[i].append(x[j])

    s[i].append(x[-1])
for i in range(n):
    print(''.join(s[i]))
