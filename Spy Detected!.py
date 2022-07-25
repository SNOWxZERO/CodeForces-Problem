n = int(input())
for i in range(0, n):
    input()
    s = list(map(int, input().split()))
    s1, s2 = set(s)
    if s[0]==s[1] :
        if s[0] == s1 :
            print(s.index(s2)+1)
        else:
            print(s.index(s1) + 1)
    elif s[1]==s[2]:
        print(1)
    else:
        print(2)
