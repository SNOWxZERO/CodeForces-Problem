n = int(input())
s = list(input())
ans = []
turn = n & 1
ans.append(s[0])
for i in range(1, n):
    if turn:
        ans.insert(0, s[i])
        turn = 0
        continue
    ans.append(s[i])
    turn = 1
print(''.join(ans))

