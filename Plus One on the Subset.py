t= int(input())
for i in range(t):
    input()
    s= list(map(int,input().split()))
    s.sort()
    print(s[-1]-s[0])