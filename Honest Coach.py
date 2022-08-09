t = int(input())
for i in range(t):
    n = int(input())
    s=list(map(int,input().split()))

    dif = 1001
    s.sort()
    for i in range(n-1) :
        dif = min(dif,s[i+1]-s[i])
        if dif == 0 :
            break
    print(dif)


