t = int(input())
for i in range(t):
    s = list(map(int, input().split()))
    ma1 = max(s[0], s[1])
    ma2 = max(s[2], s[3])
    mi1 = min(s[0], s[1])
    mi2 = min(s[2], s[3])
    if ma1 < mi2 or ma2 < mi1 :
        print('NO')
        continue
    print('YES')
