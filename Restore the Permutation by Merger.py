t = int(input())
for i in range(t):
    n = int(input())
    a = list(input().split())
    ans = []
    for i in a:
        if i in ans:
            continue
        ans.append(i)
    print(' '.join(ans))
