t= int(input())
for i in range(t):
    s= list(map(int,input().split()))
    s.sort()
    print(max(2*s[0],s[1])**2)