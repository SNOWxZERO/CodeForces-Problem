n = int(input())
answer = []
for i in range(n):
    a, b = map(int, input().split())
    if a == b:
        answer.append('0')
        continue
    c = int(abs(a - b) / 10)
    if (a - b) % 10 != 0:
        c += 1
    answer.append(str(c))
print('\n'.join(answer))
