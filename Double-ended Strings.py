def lcs(a,b,m,n):
    LCSuff = [[0 for k in range(n + 1)] for l in range(m + 1)]
    result = 0
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                LCSuff[i][j] = 0
            elif (a[i - 1] == b[j - 1]):
                LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1
                result = max(result, LCSuff[i][j])
            else:
                LCSuff[i][j] = 0
    return result


x=int(input())
z=[0 for k in range(x)]
for i in range(0,x):
    a=input()
    b=input()
    if a==b : z[i]=0
    else:
        m = len(a)
        n = len(b)
        z[i]=m+n-(2*(lcs(a,b,m,n)))
for i in z:
    print(i)

