n = int(input())
s = []
for i in range(n):
    t = input()
    if int(t) / (10 ** (len(t) - 1)) == 0:
        s.append([t])
    else:
        t = list(t)
        rlist = []
        t.reverse()
        for i in range(0, len(t)):
            if t[i] == '0':
                continue
            else:
                rlist.append(int(t[i]) * (10 ** i))
        s.append(rlist)

for i in range(n):
    print(len(s[i]))
    print(' '.join(map(str, s[i])))
