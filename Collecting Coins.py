t=int(input())
for i in range(t):
    s = list(map(int,input().split()))
    if sum(s)%3!=0:
        print('NO')
        continue
    ma = max(s[:3])
    res = (3*ma) -sum(s[:3])
    if s[3]-res < 0 :
        print('NO')
        continue

    print('YES')