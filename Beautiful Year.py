x = int(input())
x += 1
while x < 9050:
    s = str(x)
    if s[0]==s[1]:
        x=(int(x/100)+1)*100
        continue
    elif s[1] == s[2]:
        x=(int(x/10)+1)*10
        continue
    else:
        j = 0
        while j < 4:
            if s[j] == s[j - 1] or s[j] == s[j - 2] or s[j] == s[j - 3]:
                x += 1
                break
            j += 1
        if j == 4:
            print(s)
            break
