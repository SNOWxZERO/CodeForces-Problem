t = int(input())
for i in range(0, t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if k == 0 :
        print(sum(a))
        continue
    if n == k :
        a.extend(b)
        a.sort()
        print(sum(a[-n:]))
        continue

    a.sort()
    b.sort()
    for i in range(k):

        if a[i] < b[n-i-1]:
            a[i] = b[n-i-1]
        else:
            break
    #if a[0] < b[-1]:
        #a[:k] = b[-k:]
    print(sum(a))

