n = int(input())
answer = []
for i in range(n):
    input()
    s = sorted(set(map(int, input().split())))
    if len(s) == 1:
        answer.append('YES')
        continue
    for k in range(len(s) - 1):
        if s[k + 1] - s[k] > 1:
            answer.append('NO')
            break
        if k == len(s) - 2:
            answer.append('YES')

print('\n'.join(answer))
