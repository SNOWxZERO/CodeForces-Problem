s = list(input())
i = 0
turn = 0

while i < len(s) - 1:

    if s[i] == s[i + 1]:
        turn += 1
        s.pop(i + 1)
        s.pop(i)

        if i == 0:
            continue
        i -= 1
        continue
    i += 1
if turn & 1:
    print('Yes')
else:
    print('No')
